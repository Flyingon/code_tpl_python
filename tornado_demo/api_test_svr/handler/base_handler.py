# -*- coding: utf-8 -*-

import re
from functools import wraps
import json
from concurrent.futures import ThreadPoolExecutor
import traceback

import tornado.gen
from tornado.web import RequestHandler, HTTPError
from tornado.escape import json_encode, json_decode
from tornado.concurrent import run_on_executor

from util.coding_check import to_str
from log.log import app_log


def required_method(methods):
    def wrap_func(func):
        @wraps(func)
        def f(handler_obj, *args, **kwargs):
            if handler_obj.method not in methods:
                msg = "{} only".format(",".join(methods))
                handler_obj._fail_response(msg=msg)
                return
            return func(handler_obj, *args, **kwargs)

        return f

    return wrap_func


required_GET = required_method(['GET'])
required_POST = required_method(['POST'])


def handler_try(func):
    def handle_problems(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except KeyError as e:
            traceback.print_exc()
            self._fail_response(msg="请检查字段：%s" % str(e))
            return
        except Exception as e:
            traceback.print_exc()
            self._fail_response(msg=str(e))
            return

    return handle_problems


def set_csrf_headers(self, methods):
    origin = None
    if self.request.headers.get('Origin'):
        origin = self.request.headers['Origin']
    else:
        url = self.request.headers.get('Referer')
        if url:
            pat = re.compile(r'(http|https)://.+/')
            match = pat.search(url)
            origin = match.group()[0:-1]
    if origin:
        self.set_header('Access-Control-Allow-Origin', origin)
    self.set_header('Access-Control-Allow-Methods', ', '.join(methods))
    self.set_header('Access-Control-Max-Age', 1000)
    self.set_header('Access-Control-Allow-Headers',
                    'Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With')
    self.set_header('Access-Control-Allow-Credentials', 'true')


class BaseRequestHandler(RequestHandler):

    def _set_json_headers(self):
        self.set_header('Content-Type', 'application/json')

    def _success_response(self, res='', msg="", extra_data=None):
        ret = {
            "code": 0,
            "data": res,
            "msg": msg
        }
        if extra_data:
            ret.update(extra_data)
        self._json_response(ret)

    def _fail_response(self, code=-1, msg="", extra_data=None):
        ret = {
            "code": code,
            "msg": msg
        }
        if extra_data:
            ret.update(extra_data)
        self._json_response(ret)

    def _json_response(self, ret):
        return self.write(json_encode(ret))

    def _post_body_args(self):
        args = None
        if self.request.body:
            try:
                args = json_decode(self.request.body)
            except Exception as e:
                app_log.error("json_encode error: %s", str(e))
                self._fail_response(msg="request body isn't json object")
                return
        return args

    def _delist_arguments(self, args):
        for arg, value in list(args.items()):
            if len(value) == 1:
                args[arg] = to_str(value[0])
        return args

    def _post_arguments_args(self):
        args = self._delist_arguments(self.request.arguments)
        return args


class MethodDispatcher(BaseRequestHandler):
    executor = ThreadPoolExecutor(10)
    allow_methods = ()

    def set_default_headers(self):
        set_csrf_headers(self=self, methods=('POST', 'GET', 'OPTIONS'))

    @run_on_executor
    def _dispatcher(self):
        args = None

        # if self.request.arguments:
        #     args = self._delist_arguments(self.request.arguments)

        path = self.request.uri.split('?')[0]
        method = path.split('/')[-1]
        if not method.startswith('_'):
            if method not in self.allow_methods:
                raise HTTPError(404)
            func = getattr(self, method, None)
            if func:
                if args:
                    return func(**args)
                else:
                    return func()
            else:
                raise HTTPError(404)
        else:
            raise HTTPError(404)

    @tornado.gen.coroutine
    def get(self):
        self.method = 'GET'
        ret = yield self._dispatcher()
        # return self._dispatcher()

    @tornado.gen.coroutine
    def post(self):
        self.method = 'POST'
        ret = yield self._dispatcher()
        # return self._dispatcher()

    def options(self):
        self.set_status(204)
        self.finish()

    @staticmethod
    def check_params(params, check_list, type):
        """
        参数检查
        params: 上报的参数
        check_list: 检查的参数
        type: all(所有参数都需要上报); any(至少有一个参数需要上报)
        """
        if not params:
            return "上报参数为空"
        if type == 'all':
            for key in check_list:
                if not params.get(key):
                    return "参数[%s]没有上报" % key
        elif type == 'any':
            if not any([params.get(key) for key in check_list]):
                return "参数 %s 至少上报一个" % ','.join(check_list)
        return 0


class JsonPostHandler(BaseRequestHandler):
    executor = ThreadPoolExecutor(10)

    def initialize(self):
        pass

    def set_default_headers(self):
        set_csrf_headers(self=self, methods=('POST',))

    @tornado.gen.coroutine
    def post(self):
        try:
            request_data = json.loads(to_str(self.request.body))
        except Exception as e:
            app_log.error(str(e))
            self._fail_response(msg='请上报正确参数格式:json序列化,utf-8编码')
            return
        app_log.debug('request_data: %s', request_data)
        ret_data = yield self.request_process(request_data)
        app_log.debug('response_data: %s', ret_data)
        if ret_data:
            self._json_response(ret_data)

    @run_on_executor
    def request_process(self, request_data):
        ret_data = self.response(request_data)
        return ret_data

    def response(self, request_data):
        raise NotImplementedError


class HttpGetHandler(BaseRequestHandler):
    executor = ThreadPoolExecutor(10)

    def initialize(self):
        pass

    def set_default_headers(self):
        set_csrf_headers(self=self, methods=('GET',))

    @tornado.gen.coroutine
    def get(self):
        ret_data = yield self.request_process()
        app_log.debug('response_data: %s', ret_data)
        if ret_data:
            self._json_response(ret_data)

    @run_on_executor
    def request_process(self):
        ret_data = self.response()
        return ret_data

    def response(self):
        raise NotImplementedError

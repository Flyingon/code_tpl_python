# -*- coding: utf-8 -*-
import os, sys
import getopt

import os.path
import logging

import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import config
from handler.api_trans import APITrans
from log import log

conf_file = ''


def usage():
    """
    使用说明函数
    """
    print(('Usage:', sys.argv[0], '-c conf_file'))
    sys.exit(1)


def parse_command_line() -> conf_file:
    if len(sys.argv) < 3:
        usage()
    conf_file = ''
    opts, args = getopt.getopt(sys.argv[1:], "c:", [])
    for option, value in opts:
        if option == "-c":
            conf_file = value
    return conf_file


def init_app() -> tornado.web.Application:
    handlers = [
        (r"/api/tans/.*", APITrans),  # 消息转发
    ]
    settings = dict(
        cookie_secret="LxnseyfgRdCGwrTUR0OmhS8r7Aon+kq2j+GZfv0sAfo=",
        # login_url="/auth/account",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=False,
        debug=True,
        autoescape=None,
    )
    handlers += [
        (r"/server/(.*)", tornado.web.StaticFileHandler, dict(path=settings['template_path'])),
        (r"/static/(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
    ]

    return tornado.web.Application(handlers, **settings)


def main():
    config.init_config(parse_command_line())
    config.basic_conf_check()
    log.set_log_level('app_log', logging.DEBUG)
    app = init_app()
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.bind(config.server_port)
    http_server.start(config.process_num)
    tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    print(('-' * 20, 'api_test_svr start', '-' * 20))
    # asyncio.get_event_loop().run_forever()
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

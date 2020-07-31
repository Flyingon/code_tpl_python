# -*- coding: utf-8 -*-

import os
import math
import traceback
from log.log import app_log
from handler.base_handler import MethodDispatcher, handler_try, required_POST


class APITrans(MethodDispatcher):
    allow_methods = (
        'invoke',
    )

    @handler_try
    @required_POST
    def invoke(self):
        headers = self.request.headers
        params = self._post_body_args()
        app_log.info("APITrans.invoke req headers: %s, params: %s" % (headers, params))

        return

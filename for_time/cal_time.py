# -*- coding: utf-8 -*-

import time


def spend_time(old_time):
    time_now = int(round(time.time() * 1000))
    spend = time_now - old_time
    return spend

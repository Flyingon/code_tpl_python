# -*- coding: utf-8 -*-

import time


# compare_time 时间比较
def compare_time(time1, time2):
    try:
        s_time = time.mktime(time.strptime(time1, '%Y-%m-%d %H:%M:%S'))
        e_time = time.mktime(time.strptime(time2, '%Y-%m-%d %H:%M:%S'))
    # print 's_time is:', s_time
    # print 'e_time is:', e_time
    except Exception as e:
        print("[ERROR] strptime err: ", e)
        return 0
    return int(s_time) - int(e_time)

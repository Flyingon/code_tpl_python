# -*- coding: utf-8 -*-

import time
import datetime
from dateutil.relativedelta import relativedelta


# 获取num小时前的时间和下一小时的时间
def get_hour_ago_str(num):
    """
    返回num小时前0点时间戳到num-1小时前0点时间戳，精确到秒
    :return
    ts_from: num小时前0点时间戳
    ts_to: num-1小时前0点时间戳
    """
    now = datetime.datetime.now()
    hours = datetime.timedelta(hours=num)
    ago = now - hours
    ago = datetime.datetime(ago.year, ago.month, ago.day, ago.hour, 0, 0, 0)
    future = datetime.datetime(now.year, now.month, now.day, now.hour+1, 0, 0, 0)
    return ago.strftime("%Y-%m-%d %H:%M:%S"), future.strftime("%Y-%m-%d %H:%M:%S")


# 获取num天前到当前的时间戳
def get_hour_ago_ts(num):
    """
    返回num小时前0点时间戳到num-1小时前0点时间戳，精确到秒
    :return
    ts_from: num小时前0点时间戳
    ts_to: num-1小时前0点时间戳
    """
    now = datetime.datetime.now()
    one = datetime.timedelta(hours=1)
    hours = datetime.timedelta(hours=num)
    ago = now - hours
    ago = datetime.datetime(ago.year, ago.month, ago.day, ago.hour, 0, 0)
    ago_time = ago.timetuple()
    ts_from = int(time.mktime(ago_time))
    to_time = ago + one
    ts_to = int(time.mktime(to_time.timetuple()))
    return ts_from * 1000, ts_to * 1000


# 获取num天前到当前的时间戳
def get_days_ago_ts(num):
    """
    返回num天前0点时间戳到num-1天前0点时间戳，精确到秒
    :return
    ts_from: num天前0点时间戳
    ts_to: num-1天前0点时间戳
    """
    now = datetime.datetime.now()
    one = datetime.timedelta(days=1)
    days = datetime.timedelta(days=num)
    ago = now - days
    ago = datetime.datetime(ago.year, ago.month, ago.day, 0, 0, 0)
    ago_time = ago.timetuple()
    ts_from = int(time.mktime(ago_time))
    to_time = ago + one
    ts_to = int(time.mktime(to_time.timetuple()))
    return ts_from * 1000, ts_to * 1000


# 获取num周前到当前的时间戳
def get_week_ago_ts(num):
    """
    返回num周前0点时间戳到num-1周前0点时间戳，精确到秒
    :return
    ts_from: num周前0点时间戳
    ts_to: num-1周前0点时间戳
    """
    now = datetime.datetime.now()
    one = datetime.timedelta(weeks=1)
    weeks = datetime.timedelta(weeks=num)
    ago = now - weeks
    ago = datetime.datetime(ago.year, ago.month, ago.day, 0, 0, 0)
    ago_time = ago.timetuple()
    ts_from = int(time.mktime(ago_time))
    to_time = ago + one
    ts_to = int(time.mktime(to_time.timetuple()))
    return ts_from * 1000, ts_to * 1000


def get_month_ago_ts(num):
    """
    返回num月前0点时间戳到num-1月前0点时间戳，精确到秒
    :return
    ts_from: num月前0点时间戳
    ts_to: num-1月前0点时间戳
    """
    now = datetime.datetime.now()
    ago_from = now - relativedelta(months=num)
    ago_to = now
    if num > 1:
        ago_to = now - relativedelta(months=num - 1)
    ago_from = datetime.datetime(ago_from.year, ago_from.month, 1, 0, 0, 0)
    ts_from = int(time.mktime(ago_from.timetuple()))
    ago_to = datetime.datetime(ago_to.year, ago_to.month, 1, 0, 0, 0)
    ts_to = int(time.mktime(ago_to.timetuple()))

    return ts_from * 1000, ts_to * 1000


# 获取num天前到当前的时间戳
def get_duration_days_ago_ts(num):
    """
    返回num天前0点时间戳到当前同一时间点时间戳，精确到秒
    :return
    ts_from: num天前0点时间戳
    ts_to: num-1天前0点时间戳
    """
    now = datetime.datetime.now()
    duration = now - datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
    days = datetime.timedelta(days=num)
    ago = now - days
    ago = datetime.datetime(ago.year, ago.month, ago.day, 0, 0, 0)
    ago_time = ago.timetuple()
    ts_from = int(time.mktime(ago_time))
    to_time = ago + duration
    ts_to = int(time.mktime(to_time.timetuple()))
    return ts_from * 1000, ts_to * 1000


if __name__ == '__main__':
    # print(get_month_ago_ts(10))
    # print(get_week_ago_ts(10))
    # print(get_days_ago_ts(9))
    print(get_hour_ago_str(24))
    # print(get_duration_days_ago_ts(1))

# -*- coding: utf-8 -*-

import re


def re_sub():
    test_str = 'util.ReportMonitor("服务启动", 0, 1)'
    pattern = re.compile(r"util.ReportMonitor\(\".+\", (0), 1\)")
    print(pattern.findall(test_str))
    out = re.sub(pattern, '127.0.0.1', test_str)
    print(out)


def re_sub_url():
    url = 'https://113.215.20.136:9011/113.215.6.77/c3pr90ntcya0/youku/6981496DC9913B8321BFE4A4E73/0300010E0C51F10D86F80703BAF2B1ADC67C80-E0F6-4FF8-B570-7DC5603F9F40.flv'
    pattern = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    print(pattern.findall(url))
    out = re.sub(pattern, '127.0.0.1', url)
    print(out)


if __name__ == '__main__':
    re_sub()
    re_sub_url()

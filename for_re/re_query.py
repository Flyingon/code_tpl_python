# -*- coding: utf-8 -*-

import re


def re_query():
    data = "			attr.Monitor(0, 1) // 处理任务panic\n"
    match = re.match(r'.*attr\.Monitor\(0\,.+\)*[\s\t]*//[\s]*(.+)', data)
    if match:
        print(match.group(1))

    data = '	util.ReportMonitor("服务启动", 0, 1)\n'
    data = '	util.ReportMonitor("重连etcd客户端次数",0,1)'
    match = re.match(r'.*util\.ReportMonitor\(\"(.+)\", *0, *1 *\)', data)
    if match:
        print(match.group(1))

if __name__ == '__main__':
    re_query()

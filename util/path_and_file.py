# -*- coding: utf-8 -*-
import os


def get_data(file_name):
    ret = []
    if not os.path.exists(file_name):
        print("[WARNING] file[%s] is not exist" % file_name)
        return ret
    f = open(file_name, "r")
    data_list = f.readlines()
    f.close()
    for d in data_list:
        d = d.strip("\n").strip(" ")
        ret.append(d)
    return ret



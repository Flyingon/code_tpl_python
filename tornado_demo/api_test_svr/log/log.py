# coding:utf-8
import logging

# FORMAT = "%(asctime)s %(pathname)s %(filename)s %(funcName)s %(lineno)s %(levelname)s - %(message)s"
log_format = "%(asctime)s %(filename)s %(funcName)s %(lineno)s %(levelname)s - %(message)s"
date_format = '%Y-%m-%d %H:%M:%S'

logging.basicConfig(format=log_format, level=logging.INFO, datefmt=date_format)

app_log = logging.getLogger("app_log")


def set_log_level(log_name, level):
    logging.getLogger(log_name).setLevel(level)

"""Gunicorn config file.
Based on: https://gist.github.com/HacKanCuBa/275bfca09d614ee9370727f5f40dab9e
Changelog
=========
2020-08-25 init file
"""

# Gunicorn (v20.0) Configuration File
# Reference - https://docs.gunicorn.org/en/20.0.4/settings.html
#
# To run gunicorn by using this config, run gunicorn by passing
# config file path, ex:
#
#       $ gunicorn --config=gunicorn.py MODULE_NAME:VARIABLE_NAME
#

# ===============================================
#           Server Socket
# ===============================================

# bind - The server socket to bind
bind = "0.0.0.0:9080"

# backlog - The maximum number of pending connections
# Generally in range 64-2048
backlog = 2048

# ===============================================
#           Worker Processes
# ===============================================

# workers - The number of worker processes for handling requests.
# A positive integer generally in the 2-4 x $(NUM_CORES) range
workers = 1

# worker_class - The type of workers to use
# A string referring to one of the following bundled classes:
# 1. sync
# 2. eventlet - Requires eventlet >= 0.9.7
# 3. gevent - Requires gevent >= 0.13
# 4. tornado - Requires tornado >= 0.2
# 5. gthread - Python 2 requires the futures package to be installed (or
# install it via pip install gunicorn[gthread])
# 6. uvicorn - uvicorn.workers.UvicornWorker
#
# You’ll want to read http://docs.gunicorn.org/en/latest/design.html
# for information on when you might want to choose one of the other
# worker classes.
# See also: https://www.uvicorn.org/deployment/
worker_class = "uvicorn.workers.UvicornWorker"

# threads - The number of worker threads for handling requests. This will
# run each worker with the specified number of threads.
# A positive integer generally in the 2-4 x $(NUM_CORES) range
# threads = 1

# worker_connections - The maximum number of simultaneous clients.
# This setting only affects the Eventlet and Gevent worker types.
worker_connections = 1000

# max_requests - The maximum number of requests a worker will process
# before restarting
# Any value greater than zero will limit the number of requests a work
# will process before automatically restarting. This is a simple method
# to help limit the damage of memory leaks.
# max_requests = 10000

# max_requests_jitter - The maximum jitter to add to the max-requests setting
# The jitter causes the restart per worker to be randomized by
# randint(0, max_requests_jitter). This is intended to stagger worker
# restarts to avoid all workers restarting at the same time.
max_requests_jitter = 1000

# timeout - Workers silent for more than this many seconds are killed
# and restarted
timeout = 30

# graceful_timeout - Timeout for graceful workers restart
# How max time worker can handle request after got restart signal.
# If the time is up worker will be force killed.
graceful_timeout = 30

# keep_alive - The number of seconds to wait for requests on a
# Keep-Alive connection
# Generally set in the 1-5 seconds range.
keep_alive = 2

# ===============================================
#           Debugging
# ===============================================

# reload - Restart workers when code changes
reload = False

# reload_engine - The implementation that should be used to power reload.
# Valid engines are:
#     ‘auto’ (default)
#     ‘poll’
#     ‘inotify’ (requires inotify)
reload_engine = "auto"

# reload_extra_files - Extends reload option to also watch and reload on
# additional files (e.g., templates, configurations, specifications, etc.).
reload_extra_files = []

# spew - Install a trace function that spews every line executed by the server
spew = False

# check_config - Check the configuration
check_config = False

# ===============================================
#           Server Mechanics
# ===============================================

# preload_app - Load application code before the worker processes are forked
# By preloading an application you can save some RAM resources as well as
# speed up server boot times. Although, if you defer application loading to
# each worker process, you can reload your application code easily by
# restarting workers.
preload_app = False

# reuse_port - Set the SO_REUSEPORT flag on the listening socket.
reuse_port = False

# chdir - Chdir to specified directory before apps loading
chdir = ""

# daemon - Daemonize the Gunicorn process.
# Detaches the server from the controlling terminal and enters the background.
daemon = False

# pidfile - A filename to use for the PID file
# If not set, no PID file will be written.
pidfile = None

# pythonpath - A comma-separated list of directories to add to the Python path.
# e.g. '/home/djangoprojects/myproject,/home/python/mylibrary'.
pythonpath = None

# ===============================================
#           Logging
# ===============================================

# accesslog - The Access log file to write to.
# “-” means log to stdout.
accesslog = "-"

# access_log_format - The access log format
#
# Identifier  |  Description
# ------------------------------------------------------------
# h            ->  remote address
# l            -> ‘-‘
# u            -> user name
# t            -> date of the request
# r            -> status line (e.g. GET / HTTP/1.1)
# m            -> request method
# U            -> URL path without query string
# q            -> query string
# H            -> protocol
# s            -> status
# B            -> response length
# b            -> response length or ‘-‘ (CLF format)
# f            -> referer
# a            -> user agent
# T            -> request time in seconds
# D            -> request time in microseconds
# L            -> request time in decimal seconds
# p            -> process ID
# {header}i    -> request header
# {header}o    -> response header
# {variable}e  -> environment variable
# ---------------------------------------------------------------
#
# Use lowercase for header and environment variable names, and put {...}x names
# inside %(...)s. For example:
#
# %({x-forwarded-for}i)s
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# errorlog - The Error log file to write to.
# “-” means log to stderr.
errorlog = "-"

# loglevel - The granularity of Error log outputs.
# Valid level names are:
# 1. debug
# 2. info
# 3. warning
# 4. error
# 5. critical
loglevel = "info"

# capture_output - Redirect stdout/stderr to specified file in errorlog.
capture_output = False

# logger_class - The logger you want to use to log events in gunicorn.
# The default class (gunicorn.glogging.Logger) handle most of normal usages
# in logging. It provides error and access logging.
logger_class = "gunicorn.glogging.Logger"

# logconfig - The log config file to use. Gunicorn uses the standard Python
# logging module’s Configuration file format.
logconfig = None

# logconfig_dict - The log config dictionary to use, using the standard
# Python logging module’s dictionary configuration format. This option
# takes precedence over the logconfig option, which uses the older file
# configuration format.
# Format:
# https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
logconfig_dict = {}

# ===============================================
#           Process Naming
# ===============================================

# proc_name - A base to use with setproctitle for process naming.
# This affects things like `ps` and `top`.
# It defaults to ‘gunicorn’.
proc_name = "captcha"

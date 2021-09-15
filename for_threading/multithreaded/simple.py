import threading
import requests


def worker(num):
    """thread worker function"""
    print('Worker', num)


threads = []
for i in range(100):
    t = threading.Thread(target=worker(i))
    threads.append(t)
    t.start()

from concurrent.futures import ThreadPoolExecutor
import requests


def worker(num):
    """thread worker function"""
    print('Send: ', num)
    r = requests.post("http://127.0.0.1:8080", json={"num": num})
    print(r.status_code, r.text)
    # print('Worker', num)


threads = []
pool = ThreadPoolExecutor(10)

for i in range(50):
    pool.submit(worker, i)
pool.shutdown(wait=True)
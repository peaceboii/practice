import threading, multiprocessing, time

def worker():
    print("Working...")

# Threading
t = threading.Thread(target=worker)
t.start(); t.join()

# Multiprocessing
p = multiprocessing.Process(target=worker)
p.start(); p.join()

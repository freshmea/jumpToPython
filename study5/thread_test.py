import time
import threading

def long_task(times=1):
    for i in range(5):
        time.sleep(times)
        print(f"Working: {i}")

threads = []
print("Start")

for i in range(5):
    t = threading.Thread(target=long_task, args=(0.1*i,))
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()

print("end")
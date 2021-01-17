from kcu import kjson
import functools, threading

filepath = 'test.json'
thread_count = 10

print("Protecting file: {}".format(filepath))

def writeLines(d, repeat=10):
    for i in range(repeat):
        print(d['var'], i)

        kjson.save_sync(filepath, d)

threads = []

for i in range(thread_count):
    threads.append(threading.Thread(target=functools.partial(writeLines, {'var': 'val-{}'.format(i)})))

for t in threads:
    t.start()

for t in threads:
    t.join()
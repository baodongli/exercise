import gevent
from gevent.event import Event
import werkzeug.local

# import pdb; pdb.set_trace()
LOCAL = werkzeug.local.Local()
eve = {}

def task(name, value):
    LOCAL.value = value
    for _ in range(20):
        eve[name].wait()
        del eve[name]
        eve[name] = Event()
        LOCAL.value += 10
        print("Task: %s, value: %s" % (name, LOCAL.value))

if __name__ == "__main__":
    eve['task1'] = Event()
    gevent.spawn(task, "task1", 100)
    eve['task2'] = Event()
    gevent.spawn(task, "task2", 200)
    LOCAL.value = 1000
    for _ in range(20):
        eve['task1'].set()
        eve['task2'].set()
        LOCAL.value += 10
        print("Task: main, value: %s" % LOCAL.value)
        gevent.sleep(2)

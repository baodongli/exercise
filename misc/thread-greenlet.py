import gevent
from gevent import Greenlet


class task(Greenlet):
    def __init__(self, v):
        Greenlet.__init__(self)
        self.v =v
    def _task(self):
        print(self.v)
    def _run(self):
        self._task()
        raise ValueError()

if __name__ == '__main__':
    t = task(10)
    t.start()
    gevent.sleep(1)
    print("Exception occured")
    t.join()
    #gevent.sleep(2)
    #print(t.ready(), t.successful())
    #print(str(t.exception))

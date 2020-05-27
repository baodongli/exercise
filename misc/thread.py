import gevent


class task(object):
    def __init__(self, v):
        self.v =v
    def _task(self, v1):
        print(self.v, v1)
    def invoke(self, v1):
        return gevent.spawn(self._task, v1)

if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    t = task(10)
    th = t.invoke(100)
    print(th.started, th.value)
    gevent.sleep(1)
    print(th.successful(), th.value)

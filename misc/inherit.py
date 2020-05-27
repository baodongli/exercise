class A(object):
    def __init__(self, a):
        self.a = a
    def on_message(self):
        print("on_message A %s" % self.a)
    def process(self):
        self.on_message()

class B(A):
    def on_message(self):
        print("on_message B %s" % self.a)



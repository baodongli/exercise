import jinja2

class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def mul(self):
        return self.a * self.b

TPL = jinja2.Template("""
    A: {{ o['a'] }}
    B: {{ o['b'] }}
    M: {{ o.mul() }}
""")

TPL1 = jinja2.Template("""
    A: {{ o.a }}
    B: {{ o.b }}
""")

# same results
o = A(10, 20)
TPL.render(o=o)
o = {'a':100, "b": 200}
TPL.render(o=o)


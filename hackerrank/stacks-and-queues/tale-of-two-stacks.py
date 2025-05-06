class MyQueue(object):
    def __init__(self):
        self.sk1 = list()
        self.sk2 = list()    
    def peek(self):
        if not self.sk2:
            self._migrate()        
        return self.sk2[-1]      
    def _migrate(self):
        while self.sk1:
            self.sk2.append(self.sk1.pop())    
    def pop(self):
        if not self.sk2:
            self._migrate() 
        self.sk2.pop()       
    def put(self, value):
        self.sk1.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

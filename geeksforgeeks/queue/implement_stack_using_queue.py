'''
https://www.geeksforgeeks.org/implement-stack-using-queue/

'''
from queue import Queue

class Stack:
    
    def __init__(self):
        
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0
        
    def push(self, data):
        
        self.curr_size += 1
        
        self.q2.put(data)
        
        while(not self.q1.empty()):
            self.q2.put(self.q1.get())
            
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
        
    def pop(self):
        
        if(self.q1.empty()):
            return
        
        self.q1.get()
        self.curr_size -= 1
        
    
    def getTop(self):
        
        if(self.q1.empty()):
            return
        
        return self.q1.queue[0]
    
    def getSize(self):
        if(self.q1.empty()):
            return
        
        return self.curr_size
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(s.getSize())
print(s.getTop())
s.pop()
print(s.getTop())      
        
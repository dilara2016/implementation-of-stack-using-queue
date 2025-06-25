from _collections import deque
import random

class stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()


    def push(self,x):
        self.q1.append(x)


    def pop(self):
        if(not self.q1):
            return
        while(len(self.q1)!= 1):
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1


    def top(self):
        if(not self.q1):
            return
        while(len(self.q1)!=1):
            self.q2.append(self.q1.popleft())

        top = self.q1[0]
        self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

        return top
    

    def size(self):
        return len(self.q1)
    

if __name__ == '__main__':
    s = stack()
    A = ['push', 'pop', 'top']

    for i in range(10):
        A = random.choice(A)
        if A == 'push':
            value = random.randint(1,25)
            print("Value pushed: ", value)
            s.push(value)
        elif A == 'pop':
            print("value popped: ", value)
            s.pop()
        elif A == 'top':
            top = s.top()
            if top is not None:
                print("Top item is: ",value)
            else:
                print("Stack is empty")
    print("\nsize: ",s.size())
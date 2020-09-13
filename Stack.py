# Stack implementation
from array import *
class Stack():
    def __init__(self):
        self.items=[]
        self.cap=10
    def push(self,item):
        if self.isfull():
            print('The stack is full')
            return False
        else:
            n=self.items.append(item)
            print('The pushed element is :',item)
    def pop(self):
        if self.isempty():
            print('The Stack has no element')
            return False
        else:
            k=self.items.pop()
            print('The popped element is :',k)
        return k
    def peek(self):
        if self.isempty():
            print('The Stack has no element')
        else:
            return self.items[-1]

    def size(self):
        if not self.isempty():
            return  len(self.items)
        else:
            return None
    def isempty(self):
        if self.items==[]:
            return  True
        else:
            return False
    def isfull(self):
        i= self.size()
        if i==self.cap:
            return  True
        else:
            return False


'''if __name__ == '__main__':
    stack=Stack()
    k=bool(input('Enter True for push otherwise false for pop'))
    while k:
        item=int(input('Enter the element to be inserted'))
        if stack.push(item) == False:
            k=False



    else:
        print(f'The Stack size is {stack.size()} and the capacity is {stack.cap}')
        print(stack.items)
        j=bool(input('Enter True for pop otherwise false '))
        while j:
            if stack.pop()==False:
                j=False
        else:
            print(f'The Stack size is {stack.size()} and the capacity is {stack.cap}')
            print(stack.items)
    print('The peek element in stack is',stack.peek())

'''

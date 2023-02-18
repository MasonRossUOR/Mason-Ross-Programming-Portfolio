class STACK:
    def __init__(self):
        self.MaxSize = 10
        self.Contents = []
        self.RWHead = -1

    def PUSH(self,Item):
        if self.CHECKFULL():
            self.RWHead += 1
            self.Contents.insert(self.RWHead,Item)
            return self
        else:
            print("stack is full, sorry")

    def POP(self):
        if self.CHECKEMPTY():
            Popped = self.Contents[self.RWHead]
            self.Contents.pop(self.RWHead)
            self.RWHead -= 1
            return Popped
        else:
            print("Stack empty, nothing returned")

    def PEEK(self):
        if self.CHECKEMPTY():
            print("Value =",self.Contents[self.RWHead])
            return self.Contents[self.RWHead]
        else:
            print("Stack empty, nothing to see here")

    def CHECKFULL(self):
        if self.RWHead == self.MaxSize -1:
            return False
        return True

    def CHECKEMPTY(self):
        if self.RWHead == -1:
            return False
        return True

def Main():
    MyStack = STACK()
    while True:
        print(MyStack.Contents)
        print("Push, Pop, or Peek?")
        Choice = input(">").upper()
        if Choice == "POP":
            MyStack.POP()
        elif Choice == "PEEK":
            MyStack.PEEK()
        elif Choice == "PUSH":
            Value = int(input("Give Value :"))
            MyStack.PUSH(Value)

Main()
        

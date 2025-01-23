class Stack():
    

    def __init__(self):
        self.stack = []
    
    def push(self, disc):
        self.stack.append(disc)
    
    def pop(self):
        if self.stack != []:
            return self.stack.pop()


    def __repr__(self):
        return repr(self.stack)
    

    
    
    

    

if __name__ == "__main__":
    numDiscs = 6

    towerA = Stack()
    towerB = Stack()
    towerC = Stack()

    for i in range(1, numDiscs + 1):
        towerA.push(i)

    def hanoi(left, middle, right, number):
        if number == 1:
            right.push(left.pop())
        else:
            hanoi(left, middle, right, number -1)
            hanoi(left, right, middle, 1)
            hanoi(middle, right, left, number -1)
            

    hanoi(towerA, towerB, towerC, numDiscs)
    print(towerA)
    print(towerB)
    print(towerC)

   
   
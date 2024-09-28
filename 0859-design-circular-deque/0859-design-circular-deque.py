class MyCircularDeque:

    def __init__(self, size: int):
        self.arr = []
        self.arr2 = []
        self.k = size

    def insertFront(self, value: int) -> bool:
        if len(self.arr)>=self.k:
            return False
        self.arr = [value]+self.arr
        return True
        

    def insertLast(self, value: int) -> bool:
        if len(self.arr)>=self.k:
            return False
        self.arr.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.arr)==0:
            return False
        self.arr.pop(0)
        return True
        

    def deleteLast(self) -> bool:
        if len(self.arr)==0:
            return False
        self.arr.pop()
        return True

    def getFront(self) -> int:
        if len(self.arr)==0:
            return -1
        return self.arr[0]
        

    def getRear(self) -> int:
        if len(self.arr)==0:
            return -1
        return self.arr[-1]
        

    def isEmpty(self) -> bool:
        if len(self.arr)==0:
            return True
        return False

    def isFull(self) -> bool:
        return len(self.arr)==self.k

        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
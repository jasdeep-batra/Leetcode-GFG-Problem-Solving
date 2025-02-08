from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.dictt = {}  # Stores index -> number
        self.numbb = {}  # Stores number -> SortedList of indices

    def change(self, index: int, number: int) -> None:
        if index in self.dictt:
            prev = self.dictt[index]
            self.numbb[prev].remove(index)
        
        self.dictt[index] = number
        
        if number not in self.numbb:
            self.numbb[number] = SortedList([index])
        else:
            self.numbb[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.numbb or not self.numbb[number]:
            return -1
        return self.numbb[number][0]  # The first element in SortedList is the smallest

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        wait = 0
        for item in customers:
            if item[0] > time:
                time = item[0]
            wait += ((time-item[0])+item[1])
            time+=item[1]

        return wait/len(customers)

            

        
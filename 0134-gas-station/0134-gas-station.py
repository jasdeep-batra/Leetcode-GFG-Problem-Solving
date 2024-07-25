class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        arr = 0
        if sum(gas) < sum(cost):
            return -1
        ind = 0
        for i in range(n):
            arr+=(gas[i]-cost[i])
            if arr < 0:
                arr = 0
                ind = i+1  

        return ind if arr>=0 else -1

        
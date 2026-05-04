class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        crr = 0
        ind = 0
        for i in range(len(gas)):
            crr += (gas[i]-cost[i])
            if crr < 0:
                crr = 0
                ind = i+1
        
        return ind
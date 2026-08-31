class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        crr = 0 
        ind = 0
        for i, c in enumerate(cost):
            crr += gas[i] - c
            if crr < 0:
                crr = 0
                ind = i+1
        
        return ind%len(cost) if crr>=0 else -1
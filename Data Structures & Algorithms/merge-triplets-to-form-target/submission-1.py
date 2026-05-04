class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        start = [0,0,0]

        for i in range(len(triplets)):
            a1,b1,c1 = start
            a2,b2,c2 = triplets[i]
            if max(a1,a2) <=target[0] and max(b1,b2) <=target[1] and max(c1,c2) <=target[2]:
                start = [max(a1,a2),max(b1,b2),max(c1,c2)]
            
            if start == target:
                return True
        return False
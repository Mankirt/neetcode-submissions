class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(int)
        for n in nums:
            d[n]+=1
        
        res= []
        perm = []
        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 
            
            for n in d:
                if d[n]>0:
                    perm.append(n)
                    d[n]-=1
                    backtrack()

                    perm.pop()
                    d[n]+=1
        backtrack()
        return res
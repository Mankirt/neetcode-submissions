class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = [[] for i in range(len(nums)+1)]

        d = {}
        for num in nums:
            d[num] = 1 + d.get(num,0)
        
        for key in d:
            fre[d[key]].append(key)
        
        ans = []
        for i in range(len(nums),-1,-1):
            for item in fre[i]:
                ans.append(item)
                k -= 1
            if k == 0:
                return ans
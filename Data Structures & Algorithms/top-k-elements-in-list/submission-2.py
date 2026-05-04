class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = [[] for i in range(len(nums)+1)]
        d = Counter(nums)
        for key in d:
            frq[d[key]].append(key)
        res =[]
        for i in range(len(nums),-1,-1):
            for item in frq[i]:
                res.append(item)
                if len(res) == k:
                    return res
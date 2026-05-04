class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        counter = Counter(nums)
        print(count)
        for num in counter:
            count[counter[num]].append(num)
        print(count)
        res = []
        for i in range(len(nums), -1, -1):
            if count[i]:
                res.extend(count[i])
            if len(res) >= k:
                break
        
        return res
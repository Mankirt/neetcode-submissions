class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        l=1
        q=[]

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                l+=1
            else:
                heapq.heappush(q,(-l,nums[i-1]))
                l=1
        heapq.heappush(q,(-l,nums[-1]))
        print(q)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(q)[1])
        return res
            
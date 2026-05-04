class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        heapq.heapify(h)

        for num in nums:
            heapq.heappush(h,-num)
        
        for i in range(k):
            ans= heapq.heappop(h)
        return -ans
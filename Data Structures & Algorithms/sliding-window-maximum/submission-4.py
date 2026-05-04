class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        l = 0
        ans =[]
        for r in range(len(nums)):
            
            heapq.heappush(heap,[-nums[r],r])
            if r == k-1:
                ans.append(-heap[0][0])
            if r>=k:
                l+=1
                while heap[0][1]<l:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
        
        return ans
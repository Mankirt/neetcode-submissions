class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [0] * 2001
        for num in nums:
            arr[num + 1000] += 1

        for i in range(2000,-1,-1):
            k -= arr[i]
            if k <= 0:
                return i - 1000
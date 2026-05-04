class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        crr = 0
        ans = 0
        for num in nums:
            crr += num
            if crr - k in count:
                ans += count[crr-k]
            count[crr] += 1
        return ans
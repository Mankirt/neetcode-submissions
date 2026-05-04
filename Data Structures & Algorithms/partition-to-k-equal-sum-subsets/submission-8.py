class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k:return False
        target = sum(nums)/k
        nums.sort(reverse = True)
        used = [False] * len(nums)


        def backtrack(i, k , crr):
            if k == 0:
                return True
            if crr == target:
                return backtrack(0, k-1, 0)
            
            for j in range(i, len(nums)):
                if not used[j] and crr + nums[j] <= target:
                    used[j] = True
                    if backtrack(j+1, k, crr + nums[j]): return True
                    used[j] = False
            return False
        
        return backtrack(0, k , 0)



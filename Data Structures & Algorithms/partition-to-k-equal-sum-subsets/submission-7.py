class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k : return False
        used = [False] * len(nums)
        sub = sum(nums) / k
        nums.sort(reverse=True)
        def backtrack(i,k, subsum):
            if k == 0:
                return True
            if subsum == sub:
                return backtrack(0, k-1, 0)
            
            for j in range(i,len(nums)):
                if used[j] or subsum + nums[j] > sub:
                    continue
                used[j] = True
                if backtrack(j+1, k , subsum+ nums[j]) : return True
                used[j] = False
            return False
        
        return backtrack(0, k , 0)
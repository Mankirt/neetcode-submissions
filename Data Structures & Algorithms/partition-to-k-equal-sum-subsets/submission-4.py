class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k : return False
        sub = sum(nums) / k
        used = [False] *  len(nums)
        nums.sort(reverse=True)
        
        def backtrack(i,k,subsum):
            if k == 0:
                return True
            if subsum == sub:
                return backtrack(0,k-1,0)

            
            for j in range(i,len(nums)):
                if not used[j] and subsum + nums[j] <= sub:
                    used[j] = True
                    if backtrack(j+1,k,subsum+nums[j]):
                        return True
                    used[j] = False

            return False
        
        return backtrack(0,k,0)
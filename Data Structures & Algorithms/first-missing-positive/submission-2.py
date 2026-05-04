class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp = 0

        nums.append(0)
        for i in range(len(nums)):
            temp = nums[i]
            while temp > 0 and temp <= len(nums)-1 and temp != nums[temp] :
                    new_temp = nums[temp]
                    nums[temp] = temp
                    temp = new_temp
                    print(temp)
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] !=i:
                return i
        
        return len(nums)
                    
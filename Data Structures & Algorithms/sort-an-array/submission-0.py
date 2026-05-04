class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            i = j = 0
            ans = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    ans.append(arr1[i])
                    i += 1
                else:
                    ans.append(arr2[j])
                    j += 1
            while i < len(arr1):
                ans.append(arr1[i])
                i += 1
            while j < len(arr2):
                ans.append(arr2[j])
                j += 1
            return ans

        # Convert each number to a list to prepare for merging
        nums = [[num] for num in nums]

        # Iteratively merge pairs of arrays
        while len(nums) > 1:
            temp = []
            for i in range(0, len(nums), 2):
                arr1 = nums[i]
                arr2 = nums[i+1] if i+1 < len(nums) else []
                temp.append(merge(arr1, arr2))
            nums = temp

        return nums[0] if nums else []

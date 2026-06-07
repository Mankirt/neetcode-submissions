class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for i in range(len(nums)):
            new_perms = []
            for perm in perms:
                for j in range(len(perm)+1):
                    temp = perm.copy()
                    temp.insert(j,nums[i])
                    new_perms.append(temp)
            perms = new_perms
        
        return perms

            
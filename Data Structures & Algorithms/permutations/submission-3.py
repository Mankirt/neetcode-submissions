class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            temp = []
            for perm in perms:
                for i in range(len(perm)+1):
                    copy = perm.copy()
                    copy.insert(i,num)
                    temp.append(copy)
            perms = temp
        
        return perms
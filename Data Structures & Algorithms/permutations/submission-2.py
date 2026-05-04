class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            temp = []
            for p in perms:
                for i in range(len(p)+1):
                    temp_p = p.copy()
                    temp_p.insert(i,n)
                    temp.append(temp_p)
            perms = temp
        
        return perms
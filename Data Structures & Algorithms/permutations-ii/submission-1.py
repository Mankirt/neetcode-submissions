class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)


        res = []

        def backtrack(arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            for key in counter:
                if counter[key] > 0:
                    counter[key] -= 1
                    arr.append(key)
                    backtrack(arr)
                    arr.pop()
                    counter[key] += 1

        backtrack([])
        return res
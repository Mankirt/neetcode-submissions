class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        arr = []
        def backtrack(i):
            if len(arr) == k:
                ans.append(arr.copy())
                return
            if i == n+1 or len(arr) > k:
                return
            
            arr.append(i)
            backtrack(i+1)
            arr.pop()
            backtrack(i+1)
            return
        backtrack(1)
        return ans
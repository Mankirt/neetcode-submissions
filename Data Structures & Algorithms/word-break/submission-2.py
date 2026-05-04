class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # Use set for O(1) lookups
        memo = {}  # Memoization dictionary

        def check(i, j):
            if j == len(s):  # If we've reached the end of the string
                return i == j  # True if the last word matched, otherwise False

            if (i, j) in memo:  # Check if the result is already computed
                return memo[(i, j)]

            # Case where substring from s[i:j+1] is a word
            if s[i:j+1] in wordSet:
                # Either start a new word from j+1 or continue expanding the current substring
                res = check(j+1, j+1) or check(i, j+1)
            else:
                # Continue expanding the current substring
                res = check(i, j+1)

            memo[(i, j)] = res  # Store the result in memo to avoid recomputation
            return res

        return check(0, 0)

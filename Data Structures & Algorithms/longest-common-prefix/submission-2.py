class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = [""]

        i = 0
        
        while i<len(strs[0]):
            crr = strs[0][i]
            for j in range(1, len(strs)):
                if not (i<len(strs[j]) and strs[j][i] == crr):
                    return "".join(ans)
            ans.append(strs[0][i])
            i += 1
        
        return "".join(ans)

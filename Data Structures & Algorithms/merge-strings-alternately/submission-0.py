class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        l = []
        while i<len(word1) and j<len(word2):
            l.append(word1[i])
            l.append(word2[j])
            i+=1
            j+=1
        ans = "".join(l) + word1[i:] + word2[j:]
        return ans
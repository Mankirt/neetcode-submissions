class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = [0] * 26
        for i, ch in enumerate(order):
            rank[ord(ch) - ord('a')] = i
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            ind = 0
            while ind < min(len(word1), len(word2)):
                if word1[ind] != word2[ind]:
                    if rank[ord(word1[ind]) - ord('a')] > rank[ord(word2[ind]) -ord('a')]:
                        return False
                    break
                ind += 1
            if ind == len(word2) and len(word1) > len(word2):
                return False
        
        return True

        

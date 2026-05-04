class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

        def find(i,j):
            if j == len(word2) or i == len(word1):
                return max(len(word1)-i,len(word2)-j)
            if (i,j) in dp:
                return dp[(i,j)]
            

            if word1[i] == word2[j]:
                res = find(i+1,j+1)
            else:
                res = min ( 1 + find(i+1,j), 1+ find(i,j+1), 1 + find(i+1,j+1))
            
            dp[(i,j)] = res

            return res
        
        dp = {}
        return find(0,0)
            




            
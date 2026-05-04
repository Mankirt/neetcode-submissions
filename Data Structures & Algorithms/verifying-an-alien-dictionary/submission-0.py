class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        arr = [0]*26
        rank = 0
        for o in order:
            arr[ord(o)-ord('a')] = rank
            rank+=1
        

        for i in range(1,len(words)):
            j = 0
            k = 0
            while j<len(words[i-1]) and k<len(words[i]):
                if arr[ord(words[i-1][j])-ord('a')] > arr[ord(words[i][k])-ord('a')]:
                    return False
                elif arr[ord(words[i-1][j])-ord('a')] < arr[ord(words[i][k])-ord('a')]: 
                    break
                j+=1
                k+=1
            else:
                if j<len(words[i-1]) : return False
        
        return True
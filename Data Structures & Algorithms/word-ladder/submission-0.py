class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        d = defaultdict(list)

        wordList.append(beginWord)
        n = len(wordList[0])
        for word in wordList:
            for i in range(n):
                d[word[:i]+"*"+word[i+1:]].append(word)
        

        q = [beginWord]
        visit = set(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if node == endWord:
                    return res
                for j in range(n):
                    pattern = node[:j]+"*"+node[j+1:]
                    for nei in d[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            
            res+=1
        

        return 0
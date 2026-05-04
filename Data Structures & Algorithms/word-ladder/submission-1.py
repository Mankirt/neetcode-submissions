class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        n = len(beginWord)
        wordList = set(wordList+[beginWord])
        for word in wordList:
            for i in range(n):
                adj[word[:i]+"*"+word[i+1:]].append(word)
        
        q = [beginWord]
        visit = set()
        visit.add(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return res
                for j in range(n):
                    for neigh in adj[word[:j]+"*"+word[j+1:]]:
                        if neigh not in visit:
                            q.append(neigh)
                            visit.add(neigh)
            res+=1
        return 0
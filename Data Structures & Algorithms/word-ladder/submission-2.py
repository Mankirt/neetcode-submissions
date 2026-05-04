class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        wordList = set(wordList)
        wordList.add(beginWord)
        n = len(beginWord)
        for word in wordList:
            for i in range(n):
                adj[word[:i]+"*"+word[i+1:]].append(word)
        
        q = deque([beginWord])
        t = 1
        visit = set()
        visit.add(beginWord)

        while q:

            for x in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return t
                
                for j in range(n):
                    for neigh in adj[node[:j]+"*"+node[j+1:]]:
                        if neigh not in visit:
                            q.append(neigh)
                            visit.add(neigh)
            t+=1
        
        return 0
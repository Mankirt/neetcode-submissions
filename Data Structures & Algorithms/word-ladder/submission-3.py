class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        if endWord not in wordList: return 0
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                d[pattern].append(word)
        
        q = deque([beginWord])
        visit = set()
        visit.add(beginWord)
        t = 1
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return t
                for i in range(len(node)):
                    pattern = node[:i] + "*" + node[i+1:]
                    for neigh in d[pattern]:
                        if neigh not in visit:
                            q.append(neigh)
                            visit.add(neigh)
            t += 1

        return 0
        
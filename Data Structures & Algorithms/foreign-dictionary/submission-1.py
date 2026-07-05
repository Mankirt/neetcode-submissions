class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        d = defaultdict(set)

        for word in words:
            for ch in word:
                d[ch] = set()

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    d[word1[j]].add(word2[j])
                    break
            else:
                if len(word1) > len(word2):
                    return ""
        
        res = []
        visit = set()
        path = set()
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            
            path.add(node)
            for neigh in list(d[node]):
                if not dfs(neigh): return False
            path.remove(node)
            visit.add(node)
            res.append(node)
            return True


        for key in d:
            if not dfs(key): return ""
        return "".join(res[::-1])

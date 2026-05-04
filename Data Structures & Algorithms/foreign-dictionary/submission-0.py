class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)

        for word in words:
            for char in word:
                adj[char] = set()

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(len(word1)):
                if j == len(word2):
                    return ""
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            path.add(node)
            for neigh in list(adj[node]):
                if not dfs(neigh):
                    return False
            path.remove(node)
            visit.add(node)
            res.append(node)
            return True


        res = []
        visit = set()
        path = set()
        for key in adj:
            if not dfs(key): return ""
        res.reverse()
        return "".join(res)
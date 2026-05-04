class TrieNode:
    def __init__(self):
        self.children = {}
        self.lastWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        crr = self.root
        for ch in word:
            if ch not in crr.children:
                crr.children[ch] = TrieNode()
            crr = crr.children[ch]
        crr.lastWord = True

    def search(self, word: str) -> bool:

        def dfs(j, node):
            crr = node
            for i in range(j,len(word)):
                if word[i] == '.':
                    for child in crr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in crr.children:
                        return False
                    crr=crr.children[word[i]]
            return crr.lastWord

        return dfs(0,self.root)

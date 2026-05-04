class Trie:
    def __init__(self):
        self.children={}
        self.ends = False
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        crr = self.root
        for w in word:
            if w not in crr.children:
                crr.children[w] = Trie()
            crr = crr.children[w]
        crr.ends = True

    def search(self, word: str) -> bool:
        

        def backtrack(i,node):
            crr = node
            for j in range(i,len(word)):
                if word[j] == '.':
                    for child in crr.children:
                        if backtrack(j+1,crr.children[child]):
                            return True
                    return False
                else:
                    if word[j] not in crr.children:
                        return False
                    crr=crr.children[word[j]]
            
            return crr.ends
            
        return backtrack(0,self.root)

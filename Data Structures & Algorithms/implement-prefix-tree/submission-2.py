class Trie:
    def __init__(self,val=0):
        self.node = val
        self.children = {}
        self.ends = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        crr= self.root
        for w in word:
            if not w in crr.children:
                crr.children[w] = Trie(w)
            crr = crr.children[w] 
        crr.ends = True
        return


    def search(self, word: str) -> bool:
        crr = self.root
        for w in word:
            if w not in crr.children:
                return False
            crr = crr.children[w]
        return crr.ends

    def startsWith(self, prefix: str) -> bool:
        crr = self.root
        for w in prefix:
            if w not in crr.children:
                return False
            crr = crr.children[w]
        return True
        
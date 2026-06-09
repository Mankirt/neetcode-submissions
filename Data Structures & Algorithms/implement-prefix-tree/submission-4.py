class Trie:
    def __init__(self):
        self.children = {}
        self.ends = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        crr = self.root
        for ch in word:
            if ch not in crr.children:
                crr.children[ch] = Trie()
            crr = crr.children[ch]
        crr.ends = True
        return

    def search(self, word: str) -> bool:
        crr = self.root
        for ch in word:
            if ch not in crr.children:
                return False
            crr = crr.children[ch]
        return crr.ends

    def startsWith(self, prefix: str) -> bool:
        crr = self.root
        for ch in prefix:
            if ch not in crr.children:
                return False
            crr = crr.children[ch]
        return True
        
        
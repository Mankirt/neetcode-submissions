class TrieNode:
    def __init__(self):
        self.children={}
        self.lastWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        crr = self.root
        for ch in word:
            if ch not in crr.children:
                crr.children[ch] = TrieNode()
            crr = crr.children[ch]
        crr.lastWord = True

    def search(self, word: str) -> bool:
        crr = self.root
        for ch in word:
            if ch not in crr.children:
                return False
            crr = crr.children[ch]
        return crr.lastWord

    def startsWith(self, prefix: str) -> bool:
        crr = self.root
        for ch in prefix:
            if ch not in crr.children:
                return False
            crr = crr.children[ch]
        return True
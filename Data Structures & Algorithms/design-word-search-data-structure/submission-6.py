class Trie:
    def __init__(self):
        self.children = {}
        self.ends = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        crr = self.root

        for ch in word:
            if ch not in crr.children:
                crr.children[ch] = Trie()
            crr = crr.children[ch]
        crr.ends = True

    def search(self, word: str) -> bool:
        crr = self.root
        def check(node, i):
            if i == len(word):
                return node.ends
            
            if word[i] == '.':
                for child in node.children:
                    if check(node.children[child],i+1): return True
                return False
            elif word[i] not in node.children:
                return False
            else:
                return check(node.children[word[i]], i+1)
        return check(crr, 0)

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
        def backtrack(i, crr):
            if i == len(word):
                return crr.ends
            
            if word[i] != ".":
                if word[i] not in crr.children:
                    return False
                crr = crr.children[word[i]]
                return backtrack(i+1, crr)
            else:
                for child in crr.children:
                    node = crr.children[child]
                    if backtrack(i+1, node):
                        return True
                return False
        
        return backtrack(0, self.root)


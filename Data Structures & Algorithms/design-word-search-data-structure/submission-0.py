class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.eow = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        for i in range(len(word)):
            if word[i] == '.':
                for k in cur.children.keys():
                    if self.search(f"{word[:i]}{k}{word[i+1:]}"):
                        return True
                return False

            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]

        return cur.eow
        

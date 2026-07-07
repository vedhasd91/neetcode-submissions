class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.add_word(w)

        row = len(board)
        col = len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if ( r<0 or c<0 or r==row or c==col or (r,c) in visit or
                board[r][c] not in node.children
            ):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word = word+board[r][c]
            if node.is_word:
                res.add(word)

            

            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            visit.remove((r,c))

        for r in range(row):
            for c in range(col):
                dfs(r,c, root, "")


        return list(res)



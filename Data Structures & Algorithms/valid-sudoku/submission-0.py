class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])

        rset = set()
        cset = set()

        for i in range(0, rows):
            for j in range(0, cols):
                elem = board[i][j]

                if elem.isnumeric():
                    if elem not in rset:
                        rset.add(elem)
                    else:
                        return False
            rset.clear()
                

        for j in range(0, cols):
            for i in range(0, rows):
                elem = board[i][j]

                if elem.isnumeric():
                    if elem not in cset:
                        cset.add(elem)
                    else:
                        return False
            cset.clear()

        sq_dict = {}
        for i in range(0, rows):
            for j in range(0, cols):
                elem = board[i][j]

                sq = (i//3)*3 + j//3

                
                if elem.isnumeric():
                    sq_set = sq_dict.get(sq, set())
                    if elem not in sq_set:
                        sq_set.add(elem)
                        sq_dict[sq] = sq_set
                    else:
                        return False
            # print("\n")

        return True
        

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
     
        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element !=".":
                    if element in rows[i] or element in cols[j] or element in boxes[(i//3,j//3)]:
                        return False
                    boxes[(i//3,j//3)].add(element)
                    rows[i].add(element)
                    cols[j].add(element)

        
        

        return True

        

        

            

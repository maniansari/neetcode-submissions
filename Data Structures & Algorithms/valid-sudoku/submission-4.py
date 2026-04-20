
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(list)
        for col in zip(*board):
            filtered= [x for x in col if x !="."]
            if len(filtered) != len(set(filtered)):
                return False
                
        for row in board:
            filtered= [x for x in row if x !="."]
            if len(filtered) != len(set(filtered)):
                return False

        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element !=".":
                    boxes[(i//3,j//3)].append(element)

        
        for i in boxes.values():
             if len(i) != len(set(i)):
                return False

        return True

        

        

            

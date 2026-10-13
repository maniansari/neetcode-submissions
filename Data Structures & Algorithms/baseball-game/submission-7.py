class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total=0
        record=[]
        for i in range(len(operations)):
            match operations[i]:
                case 'C':
                    record.pop()
                case 'D':
                    record.append(int(record[-1])*2)
                case '+':
                    record.append(int(record[-1])+int(record[-2]))
                case _:
                    record.append(int(operations[i]))

        return sum(record)
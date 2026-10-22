class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result=[]
        ops = {
                 '+': lambda a, b: a + b,
                  '-': lambda a, b: a - b,
                  '*': lambda a, b: a * b,
                 '/': lambda a, b: int(a / b)
        }
        for i in range(len(tokens)):
            if tokens[i] in ops:
                a=result.pop()
                b=result.pop()
                result.append(ops[tokens[i]](b,a))
                
            else:
                result.append(int(tokens[i]))

        return result[-1]
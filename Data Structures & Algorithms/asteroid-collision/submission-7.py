class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result=[]
        for i in range(len(asteroids)):
            while result and result[-1] > 0 and asteroids[i] < 0:
                if result and result[-1] * asteroids[i] < 0:
                    if abs(result[-1]) > abs(asteroids[i]):
                        break
                    elif abs(result[-1]) == abs(asteroids[i]):
                        result.pop()
                        break
                    else:
                        result.pop()
                        
            else:
                result.append(asteroids[i])
        return result
        
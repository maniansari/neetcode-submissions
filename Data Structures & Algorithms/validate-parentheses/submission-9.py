class Solution:
    def isValid(self, s: str) -> bool:
        openings=[]
        if(len(s)%2!=0):
            return False
        
        pairs = {')': '(', '}': '{', ']': '['}
        for i in range(len(s)):
            if s[i] in pairs:
                if openings and openings[-1]==pairs[s[i]]:
                    openings.pop()
                else:
                    return False
            else:
                openings.append(s[i])
        return len(openings)==0

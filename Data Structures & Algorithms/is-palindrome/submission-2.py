class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        answer= []
        for char in s:
            if char.isalnum():
                answer.append(char)
        answer= "".join(answer)
        return answer==answer[::-1]


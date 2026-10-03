class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size=max(len(word1),len(word2))
        new=""
        for i in range(size):
            if i < len(word1):
                new += word1[i]
            if i < len(word2):
                new += word2[i]
        return new


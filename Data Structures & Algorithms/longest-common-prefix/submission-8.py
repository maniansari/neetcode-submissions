class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest=""
        first=strs[0]
        for word in strs:
            while not word.startswith(first):
                first=first[:-1]
                longest=""
            if word.startswith(first):
                longest=first
            
        return longest

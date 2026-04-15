from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers=defaultdict(list)
        for i in strs:
            dort=tuple(sorted(i))
            answers[dort].append(i)
        real=answers.values()
        print(real)
       
        return list(real)
        


        
        
        
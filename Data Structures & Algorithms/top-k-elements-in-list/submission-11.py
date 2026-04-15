from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answers=defaultdict(int)
        shit=[]
        for i in nums:
            answers[i]+=1
        answers = sorted(answers.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            shit.append(answers[i][0])
        return shit
        


        
            
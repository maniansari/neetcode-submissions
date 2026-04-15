from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        indices=[]
        numbers=[]
        for combo in combinations(nums,2):
            if target==combo[0]+combo[1]:
                numbers.append(combo[0])
                numbers.append(combo[1])
                break
        for i in range(len(nums)):
            if nums[i] == numbers[0]:
                if i not in indices:
                    indices.append(i)
            if nums[i] == numbers[1]:
                if i not in indices:
                    indices.append(i)   
        indices.sort()       
        return indices        



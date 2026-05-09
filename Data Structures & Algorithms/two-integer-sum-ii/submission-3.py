class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices=[]
        nums=[]
        for combo in combinations(numbers,2):
            if target==combo[0]+combo[1]:
                nums.append(combo[0])
                nums.append(combo[1])
                break
        for i in range(len(numbers)):
            if numbers[i] == nums[0]:
                if i+1 not in indices:
                    indices.append(i+1)
            if numbers[i] == nums[1]:
                if i+1 not in indices:
                    indices.append(i+1)   
        indices.sort()       
        return indices 
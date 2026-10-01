class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj=len(nums)/3
        counts = {}
        output=[]
        for i in nums:
            counts[i]=counts.get(i,0)+1

        for key, value in counts.items():
            if value >maj:
                output.append(key)
        return output
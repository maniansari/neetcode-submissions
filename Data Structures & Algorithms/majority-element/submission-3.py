class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=len(nums)/2
        counts = {}
        for i in nums:
            counts[i]=counts.get(i,0)+1

        for key, value in counts.items():
            if value >=maj:
                return key
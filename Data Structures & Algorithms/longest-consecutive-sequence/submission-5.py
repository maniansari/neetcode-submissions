class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=sorted(nums)
        count=0
        maxCount=0
        if not nums:
            return 0
        for i in nums:
            if i+1 in nums:
                count+=1
            else:
                count=0
            if count>maxCount:
                maxCount=count
        return maxCount+1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        p=len(nums)-1
        while p>=0:
            if p>0:
                if nums[p]==nums[p-1]:
                    nums.pop(p)
            p-=1
        k=len(nums)
        return k


        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=0
        output=[]
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            if i==0:
                total+=nums[i]
            else: 
                total=total*nums[i]
        for i in range(len(nums)):
            if 0 in nums:
                if nums[i]==0 and nums.count(0)==1:
                    output.append(total)
                else:
                    output.append(0)      
            else:
                output.append(int(total/nums[i]))
        return output
            
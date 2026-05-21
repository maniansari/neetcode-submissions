class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        numbers=set()
        target=0
        nums=sorted(nums)
        print(nums)
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            
            while left < right:
                temp=[]
                if (nums[i]+nums[left]+nums[right])==0:
                    print(nums[i], nums[left], nums[right])
                    temp.append(nums[i])
                    temp.append(nums[left])
                    temp.append(nums[right])
                    
                    temp=tuple(temp)
                    numbers.add(temp)
                    right-=1
                    left+=1
                elif (nums[i]+nums[left]+nums[right])>0:
                    right-=1
                elif (nums[i]+nums[left]+nums[right])<0:
                    left+=1
            
        return [list(numbers) for numbers in numbers]
       

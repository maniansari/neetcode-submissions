class Solution:
   def devide(self,arr):
        if len(arr)<=1:
            return arr
        mid = len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        leftSorted=self.devide(left)
        rightSorted=self.devide(right)

        return self.merge(leftSorted, rightSorted)



   def merge(self,left, right):
        result=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        
        result.extend(left[i:])
        result.extend(right[j:])

        return result

   def sortArray(self, nums: List[int]) -> List[int]:
        return self.devide(nums)
    
  


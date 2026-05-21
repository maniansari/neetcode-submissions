class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        current=0
        left=0
        right=len(heights)-1
    
        while left < right:
            current= min(heights[left], heights[right]) * (right - left)
            if current > max:
                max=current
            if heights[right] > heights[left]:
                left +=1
            else:
                right-=1
        return max


        
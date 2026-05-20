class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        current=0

        for i,j in combinations(range(len(heights)),2):
            current=min(heights[i], heights[j]) * (j-i)
            if current>max:
                max=current
        return max

        
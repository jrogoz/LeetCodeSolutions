class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Given: List of integers that represent height of vertical lines
        Expected result: Return maximum of water that is possible to contain between two lines

        More about: https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150
        """
        
        left = 0
        right = len(height) - 1

        max_con = 0 

        while left < right:
            # calculate current volume of container
            tmp = min(height[left], height[right]) * (right - left)

            if tmp > max_con:
                max_con = tmp

            # move the pointer that corresponds to the lower value
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_con

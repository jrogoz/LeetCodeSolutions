class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Given: Integer array nums and integer val
        Expected result: Remove all occurrences of val in nums, return number of elements in nums which are not equal to val

        More about: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
        """
        if len(nums) == 0:
            return 0

        temp = 0
        for num in nums:
            if num != val:
                nums[temp] = num
                temp += 1
        return temp
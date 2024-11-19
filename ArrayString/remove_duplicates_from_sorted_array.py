class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Given: Integer array nums sorted in non-decreasing order
        Expected result: Remove all duplicates in nums (each value must appear only once), return number of unique elements in nums

        More about: https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
        """
        if len(nums) == 0:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Given: Integer array nums sorted in non-decreasing order
        Expected result: Remove some duplicates in nums (each value can appear at most twice), return number of elements in nums after changes

        More about: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
        """
        k = 1
        reps = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if reps >= 2:
                    continue
                reps += 1
            else:
                reps = 1
            nums[k] = nums[i]
            k += 1
       
        return k

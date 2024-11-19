class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Given: Two arrays sorted in non-decreasing order.
        Expected result: Merge arrays into one sorted in non-decreasing order.

        More about: https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        
        nums1.sort()
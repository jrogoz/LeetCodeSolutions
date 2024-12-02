class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Given: Non-decreasing int list numbers and sum of two values 
        Expected result: Find two values such that their sum is equal to the given target and return their indices
        Additional condition: Index numbering starts with 1

        More about: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150
        """

        for i in range(len(numbers)):
            # determine the second value 
            rest = target - numbers[i]  

            if rest not in numbers:
                continue

            for j in range(len(numbers)):
                if numbers[j] == rest and j != i:
                    # first number must be lower than the second
                    return sorted([i+1, j+1])  
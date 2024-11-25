class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given: Array s 
        Expected result: Remove all non-alphanumerical values and return if the result is palindrome or not

        More about: https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
        """

        new_s = ''.join([item for item in s.lower() if item.isalnum()])
        return new_s == new_s[::-1]
    


        

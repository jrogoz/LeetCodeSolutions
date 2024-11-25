class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Given: Two strings s and t
        Expected result: Return true if s is a subsequence of t, or false otherwise.

        More about: https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
        """

        start = 0
        for item in s:
            if item not in t[start:]:
                return False
            j = start
            for i in range(start, len(t)):
                j += 1
                if item == t[i]:
                    start = j
                    break
        return True         
        
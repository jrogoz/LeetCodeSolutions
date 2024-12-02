from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Given: two strings ransomeNote and magazine
        Expected result: Return true if ransomeNote can be constructed using magazine letters and false otherwise

        More about: https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
        """

        # create defaultdict containers to get default values for new keys
        ransom_dict = defaultdict(int)
        magazine_dict = defaultdict(int)

        # group letters in ransomeNote
        for char in ransomNote:
            ransom_dict[char] += 1

        # group letters in magazine 
        for char in magazine:
            magazine_dict[char] += 1
        
        # check if ransomeNote can be creaconstructed using magazine letters
        for char in ransom_dict.keys():
            if ransom_dict[char] > magazine_dict[char]:
                return False
        return True
"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_dict = {}
        for rn in ransomNote:
            if rn in rn_dict:
                rn_dict[rn] += 1
            else:
                rn_dict[rn] = 1
        
        rn_dict_keys= rn_dict.keys()
        for m in magazine:
            if m in rn_dict_keys:
                if rn_dict[m] > 0:
                    rn_dict[m] -= 1

        for k in rn_dict_keys:
            if rn_dict[k] > 0:
                return False

        
        return True
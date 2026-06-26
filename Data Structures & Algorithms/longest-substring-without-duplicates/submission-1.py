class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        left = 0
        right = 1
        longest = 0
        while right <= len(s):
            substr = s[left:right]

            if len(substr) != len(set(substr)):
                left += 1
            else:
                longest = max(len(substr), longest)

            right += 1


        return longest
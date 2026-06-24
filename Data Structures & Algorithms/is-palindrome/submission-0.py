import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        reverse = ''

        i = len(s) - 1

        while i >= 0:
            reverse = reverse + s[i]
            i = i - 1

        return s == reverse
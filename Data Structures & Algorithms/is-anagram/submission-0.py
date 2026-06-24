class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {_ for i in s}
        t_dict = {_ for i in t}

        print(s_dict)
        print(t_dict)
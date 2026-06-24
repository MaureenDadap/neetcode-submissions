class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {i:0 for i in s}
        t_dict = {i:0 for i in t}

        print(s_dict)
        print(t_dict)
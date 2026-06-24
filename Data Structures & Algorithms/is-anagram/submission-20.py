class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {i:len([s if s == i else 0]) for i in s}
        t_dict = {i:len([t if t == i else 0]) for i in t}

        print(s_dict)
        print(t_dict)

        return s == t
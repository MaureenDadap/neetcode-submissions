class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict(s)
        t_dict = dict(t)

        print(s_dict)
        print(t_dict)
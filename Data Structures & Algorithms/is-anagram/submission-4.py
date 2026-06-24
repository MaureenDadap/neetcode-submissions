class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict(i for i in enumerate(s))
        t_dict = dict(enumerate(t))

        print(s_dict)
        print(t_dict)
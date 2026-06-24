class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {i:0 for i in range(0,10)}
        t_dict = dict(enumerate(t))

        print(s_dict)
        print(t_dict)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        t = jam
        s = amj

        dict() = {j:1, a:1, m:1}

        test = {"j":1, "a":1, "m":1}
        test1 = {"j":1, "a":1, "m":1}

        isso é true
        """

        if len(s) != len(t):
            return False
        
        d_S, d_T = {}, {}

        for i in range(len(s)):
            d_S[s[i]] =+ 1
            d_T[t[i]] =+ 1
        return d_S == d_T


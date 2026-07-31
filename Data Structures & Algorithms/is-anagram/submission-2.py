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
        
        countS, countT = {}, {}

        for i in range(len(s)):
            if s[i] in countS:
                countS[s[i]] += 1
            else: 
                countS[s[i]] = 1

            if t[i] in countT:
                countT[t[i]] += 1
            else: 
                countT[t[i]] = 1
        
        return countS == countT

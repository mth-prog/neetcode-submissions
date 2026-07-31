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
            countS[s[i]] = 1 + countS.get(s[i], 0)  # "Busque o valor da chave 'r'. Se não achar, me dê 0"

            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT

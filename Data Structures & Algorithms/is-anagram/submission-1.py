class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = dict()
        tMap = dict()
        n = len(s)

        if n != len(t):
            return False

        for i in range(n):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        return sMap == tMap
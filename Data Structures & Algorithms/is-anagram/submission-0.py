class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            sDict[sChar] = sDict.get(sChar, 0) + 1
            tDict[tChar] = tDict.get(tChar, 0) + 1

        return tDict == sDict
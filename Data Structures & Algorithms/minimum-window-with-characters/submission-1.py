class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        strings = {}
        window = {}

        l = 0
        minval = float('inf')
        for c in t:
            strings[c] = 1+strings.get(c,0)
        
        have = 0
        need = len(strings)
        res = [-1,-1]
        for r in range(len(s)):
            window[s[r]] = 1+window.get(s[r],0)
            if s[r] in strings and window[s[r]] == strings[s[r]]:
                have+=1
            while need == have:
                if (r-l+1)<minval:
                    minval = r-l+1
                    res = [l,r]
                
                window[s[l]]-=1
                if s[l] in strings and window[s[l]]<strings[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l : r + 1] if minval != float("infinity") else ""
            

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not self.alphafun(s[l]):
                l+=1
            while l<r and not self.alphafun(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True 
    def alphafun(self,c):
        return(ord("a")<=ord(c)<=ord("z") or ord("A")<=ord(c)<=ord("Z") or ord("0")<=ord(c)<=ord("9"))
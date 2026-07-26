class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res+=str(l)+"#"+s
            
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i = 0
        while i< len(s):
            j = i
            while s[j]!="#":
                j+=1
            length= int(s[i:j])
            j+=1
            i = j+length
            res.append(s[j:i])
            print(s[j:i])
        return res

            




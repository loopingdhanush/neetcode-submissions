class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            dic[n] = 1 + dic.get(n,0)
        for key,v in dic.items():
            freq[v].append(key)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26  
            
            for c in s:
                idx = ord(c) - ord("a")
                count[idx] += 1
            
            k = tuple(count)
            res[k].append(s)
        
        return res.values()

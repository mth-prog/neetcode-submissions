class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        indices = {}
        
        for num in nums:
            indices[num] = 1 + indices.get(num, 0)

        arr = []
        for num, val in indices.items(): 
            arr.append([val, num])
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

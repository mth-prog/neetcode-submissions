class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """a ideia é fazer uma comparação mas nao pode olhar para si mesmo usando hash map"""

        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n

            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
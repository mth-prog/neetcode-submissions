class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        [1,2,3,1] dois ponteiros i = 0 e j = i + 1
        """

        for i in range(0, len(nums)):
            for j in range(i + 1):
                if nums[i] == nums[j]:
                    return True
        return false
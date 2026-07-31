class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        [1,2,3,1] dois ponteiros i = 0 e j = i + 1
        """

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        [1,2,3,1] dois ponteiros i = 0 e i = i + 1

        """

        l1 = 0 
        l2 = 1 
        for i in range(0, len(nums)):
            if nums[l1] == nums[l2]:
                return True
            else:
                l1 =+ 1
                l2 =+ 1
        return False
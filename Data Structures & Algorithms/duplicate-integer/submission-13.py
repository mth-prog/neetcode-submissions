class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        [1,2,3,1] dois ponteiros i = 0 e j = i + 1
        """
        set_nums = set()

        for num in nums: 
            if num in set_nums:
                return True 
            set_nums.add(num)
        return False
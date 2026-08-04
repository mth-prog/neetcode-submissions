class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        final_list = []

        while i < j: 
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                j = j - 1 
                


               
            
        
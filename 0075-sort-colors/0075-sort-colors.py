class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        k = 0
        for i in range(n):
            if nums[i] == 1 :
                i += 1
            else :
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
        for i in range(n):
            if nums[i] == 2 :
                i += 1
            else :
                nums[i],nums[k] = nums[k],nums[i]
                i += 1
                k += 1
        return nums            

        
        
        
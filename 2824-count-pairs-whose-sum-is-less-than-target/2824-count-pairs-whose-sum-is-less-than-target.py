class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(0,n-1):
            for j in range (i+1,n):
                if nums[i] +nums[j] <target :
                    cnt +=1 

        return cnt            


        
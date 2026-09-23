class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        lst = []
        arr = []
        a = []
        for i in nums:
            if i > pivot :
                lst.append(i)
            elif i == pivot :
                arr.append(i)
            else :
                a.append(i)
                    
        return a + arr + lst            



        
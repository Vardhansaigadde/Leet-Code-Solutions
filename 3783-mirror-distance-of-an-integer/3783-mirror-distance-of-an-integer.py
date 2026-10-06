class Solution:
    def mirrorDistance(self, n: int) -> int:
        i = n
        rev = 0
        while n != 0 :
            rem = n%10
            rev = rev*10 + rem
            n = n//10
        return abs(i - rev)    


            
        
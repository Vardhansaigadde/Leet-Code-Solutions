class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        add = 0
        addi = 0
        count = 0
        n = len(arr)
        for i in range(0,k):
            addi += arr[i]
        if (addi/k) >= threshold :
            count +=1  
        l =0 
        r = k
        
        while r<n :
            addi += arr[r] - arr[l]
            if (addi/k) >= threshold :
                count +=  1
            l += 1
            r += 1

        return (count)           

        
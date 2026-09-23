class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = word
        k = s.find(ch)
        s1 = s[:k+1]
        return s1[::-1] +s[k+1::]

        
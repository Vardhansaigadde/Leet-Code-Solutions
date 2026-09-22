class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        res = []

        pCount = [0] * 26
        windowCount = [0] * 26

        for ch in p:
            pCount[ord(ch) - ord('a')] += 1

        for i in range(len(p)):
            windowCount[ord(s[i]) - ord('a')] += 1

        if pCount == windowCount:
            res.append(0)

        left = 0

        for right in range(len(p), len(s)):

            windowCount[ord(s[right]) - ord('a')] += 1

            windowCount[ord(s[left]) - ord('a')] -= 1

            left += 1

            if pCount == windowCount:
                res.append(left)

        return res
        
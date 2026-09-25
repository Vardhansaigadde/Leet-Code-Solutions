class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def find_first():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1      # search left part
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def find_last():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1       # search right part
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        first = find_first()

        if first == -1:
            return [-1, -1]

        last = find_last()
        return [first, last]
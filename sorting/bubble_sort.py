class Solution:
    def bubble_sort(self,nums):
        for i in range(len(nums)):
            is_sorted = True
            for j in range(len(nums)-(i+1)):
                if nums[j]>nums[j+1]:
                    is_sorted = False
                    nums[j],nums[j+1]=nums[j+1],nums[j]
            if is_sorted:
                return

obj = Solution()
nums = [12, 46, 24, 52, 20, 9]
obj.bubble_sort(nums)
print(nums)

# Time Complexity : O(n²), Best Case : O(n) (with is_sorted technique)
# Space Complexity : O(1)
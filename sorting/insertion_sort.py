class Solution:
    def insertion_sort(self,nums):
        for i in range(1,len(nums)):
            key = nums[i]
            j = i-1
            while j>=0 and key < nums[j]:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key

obj = Solution()
nums = [12, 46, 24, 52, 20, 9]
obj.insertion_sort(nums)
print(nums)

# Time Complexity:
# Best Case    : O(n)
# Average Case : O(n²)
# Worst Case   : O(n²)

# Space Complexity:
# O(1)
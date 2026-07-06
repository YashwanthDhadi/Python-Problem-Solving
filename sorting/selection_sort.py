class Solution:
    def selection_sort(self,nums):
        for i in range(len(nums)-1):
            min_pos = i
            for j in range(i+1,len(nums)):
                if nums[min_pos]>nums[j]:
                    min_pos = j
            nums[i],nums[min_pos]=nums[min_pos],nums[i]

obj = Solution()
nums = [12, 46, 24, 52, 20, 9]
obj.selection_sort(nums)
print(nums)
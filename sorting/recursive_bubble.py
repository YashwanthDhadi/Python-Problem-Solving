class Solution :
    def rec_bubble(self,arr,n):
        if n == 1:
            return
        is_sorted = True
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                is_sorted = False
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if is_sorted:
            return
        return self.rec_bubble(arr,n-1)

obj = Solution()
arr = [12, 46, 24, 52, 20, 9]
n = len(arr)
obj.rec_bubble(arr,n)
print(arr)
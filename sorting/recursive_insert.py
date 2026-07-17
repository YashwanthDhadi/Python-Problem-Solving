class Solution :
    def insert(self,arr,i,n):
        if n == 1:
            return
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        return self.insert(arr,i+1,n-1)

obj = Solution()
arr = [12, 46, 24, 52, 20, 9]
n = len(arr)
i=1
obj.insert(arr,i,n)
print(arr)
class Rotation:
    def rotation(self,arr,left,right):
        while left < right :
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
    def left_rotation(self,arr,k):
        n = len(arr)
        d = n-k
        self.rotation(arr,0,d-1)
        self.rotation(arr,d,n-1)
        self.rotation(arr,0,n-1)
        return arr
    def right_rotation(self,arr,k):
        n = len(arr)
        d = n-k
        self.rotation(arr,d,n-1)
        self.rotation(arr,0,d-1)
        self.rotation(arr, 0,n-1)
        return arr
    def specific_rotation(self,arr,k,direction):
        if direction.lower()=='right':
            self.right_rotation(arr,k)
            return arr
        else:
            self.left_rotation(arr,k)
            return arr

rotating = Rotation()
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
direction = 'right'
print(rotating.specific_rotation(arr,k,direction))

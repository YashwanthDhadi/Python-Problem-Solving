class Rotations:
    def reverse_array(self,arr,left,right):
        while left < right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
    def left_rotation(self,arr,k):
        n = len(arr)
        self.reverse_array(arr,0,k-1)  #reversing block_A
        self.reverse_array(arr,k,n-1) #reversing block_B
        self.reverse_array(arr,0,n-1) #reverse entire array
        return arr
    def right_rotation(self,arr,k):
        n = len(arr)
        self.reverse_array(arr,n-k,n-1)      #reversing block_B
        self.reverse_array(arr,0,n-k-1)  #reversing block_A
        self.reverse_array(arr,0,n-1)     #reverse entire array
        return arr

arr = [1,2,3,4,5]
k=2
rotation = Rotations()
left_rotation = rotation.left_rotation(arr.copy(),k)
right_rotation = rotation.right_rotation(arr.copy(),k)
print(left_rotation)
print(right_rotation)

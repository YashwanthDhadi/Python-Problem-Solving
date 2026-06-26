def at_beginning(arr,value):
    arr.insert(0,value)
def at_last(arr,value):
    arr.append(value)
def at_position(arr,position,value):
    arr.insert(position,value)

arr = [1,2,3,4,5]
at_beginning(arr,6)
at_last(arr,7)
at_position(arr,4,8)
print(arr)



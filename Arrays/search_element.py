def search_element(arr,key):
    if  key not in arr:
        return "Key Not found"
    return arr.index(key)

arr = [6,7,9,5,3,10]
key = 5
print(search_element(arr,key))
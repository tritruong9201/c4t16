def binary_search(arr,l,r,n):
    if r>l: 
        mid=l+(r-l)//2
        if arr[mid] == n :
            return mid
        elif arr[mid] < n :
            return binary_search(arr,mid+1,r,n)
        elif arr[mid] > n :
            return binary_search(arr,l,mid-1,n)
    else:
        return -1
# result = binary_search(arr,1,len(arr),n)
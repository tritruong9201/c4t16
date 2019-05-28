def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] >= arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
arr=[54,76,23,54,65,32,65,87,-76,-54,-43]
bubbleSort(arr)
for x in arr:
    print(x, end=", ")
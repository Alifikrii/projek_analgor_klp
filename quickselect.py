def partition(arr, l, r) :
     
    x = arr[r]
    i = l
    for j in range(l, r) :
         
        if arr[j] <= x :
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
             
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthSmallest(arr, l, r, k) :
    if (k > 0 and k <= r - l + 1):
        index = partition(arr, l, r)
 
        if (index - l == k - 1) :
            return arr[index]
 
        if (index - l > k - 1) :
            return kthSmallest(arr, l, index - 1, k)
 
        return kthSmallest(arr, index + 1, r,
                            k - index + l - 1)
    print("Index out of bound")

arr = [ 10, 4, 5, 8, 6, 11, 26, 30 ] #4 5 6 8 10 11 26 30
                                     #0 1 2 3  4  5  6  7
n = len(arr)

if (n%2==0) :
    median1 = (kthSmallest(arr, 0, n - 1, n/2))
    median2 = (kthSmallest(arr, 0, n - 1, (n-1)/2))
    print(median1)
    print(median1)
else :
    median = (n+1)/2
    print("Median is ", end = "")
    print(kthSmallest(arr, 0, n - 1, median))
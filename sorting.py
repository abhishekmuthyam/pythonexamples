class Sorting:
    
    def mergeFun(arr1,arr2, res, arr1Len, arr2Len): 
        i, j, k = 0, 0, 0
        while (i < arr1Len): 
            res[k] = arr1[i] 
            i += 1
            k += 1
        while (j < arr2Len): 
            res[k] = arr2[j] 
            j += 1
            k += 1
       
        res.sort()
        print(list(set(res)))


arr1 = [ 8, 7, 9,6 ] 
arr2 = [ 6, 8, 10,5] 
arr1Len = len(arr1) 
arr2Len = len(arr2)
arrayLen = arr1Len +arr2Len
  
res = [0 for i in range(arr1Len + arr2Len)]

Sorting.mergeFun(arr1, arr2, res, arr1Len, arr2Len)

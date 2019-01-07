def sortedMerge(arr1,arr2, res, arr1Len, arr2Len): 
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

def removeDups(res, arrayLen):
    mp = {i : 0 for i in res}
    for i in range(arrayLen):
        if mp[res[i]] == 0:
            print(res[i], end =" ")
            mp[res[i]] = 1
        

arr1 = [ 5, 7, 9,6 ] 
arr2 = [ 6, 8, 10,5] 
arr1Len = len(arr1) 
arr2Len = len(arr2)
arrayLen = arr1Len +arr2Len
  
res = [0 for i in range(arr1Len + arr2Len)]

sortedMerge(arr1, arr2, res, arr1Len, arr2Len)

removeDups(res,arrayLen)


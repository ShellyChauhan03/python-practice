"""Given a sorted array arr[] of n elements, write a
function to search a given element x in arr[]. Do it using linear
and binary search techniques."""

arr = [2,6,9,12,25,36,40]
x = int(input('x: '))
print('Find',x,' in arr:',arr)
# binary search

def bin_search(ar, n, start, end):
    #print('bin_search',start,'-',end)
    mid = (int)((end+start)/2)
    if start<end :
        if n == ar[mid]:
            return 'Found n'
        else:
            if n > ar[mid]:
                return bin_search(ar,n,mid+1,end)
            else:
                return bin_search(ar,n, start, mid-1)
    else:
        return 'Not found!'

def lin_search(ar, n, start, end):
    for i in range(0,end):
        if n == ar[i]:
            return 'Found n'
    return 'Not Found!'


print('calling function',arr[0])
res = lin_search(arr,x, 0, len(arr))
print('Linear search',res)
bres = bin_search(arr,x,0,len(arr))
print('Binary search',bres)

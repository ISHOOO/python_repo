arr=[12,23,28,31,33,48,50,59,63]
search=48
def binsearch(arr,search):
    start,end=0,len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==search:
            return mid
        elif search>arr[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1
print(binsearch(arr,search))
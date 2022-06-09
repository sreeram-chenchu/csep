def binary(arr,l,h,k):
    while(l<=h):
        middle=(l+h)//2
        if(arr[middle]==k):
            return middle
        elif(arr[middle]>k):
           return binary(arr,l,middle-1,k)
        else:
            return binary(arr,middle+1,h,k)
    return -1
arr=[11,3,4,20,5,6,9,10]
k=20
x=binary(arr,0,len(arr)-1,k)
if(x!=-1):
    print("The value index at",x)
else:
    print("Not Found")        

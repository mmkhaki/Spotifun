arr1=[1,5,3,6,4,8]
arr2=[]
target=6
for i in range(len(arr1)):
    if(len(arr1)==0):
        break
    arr11=arr1[-1]
    if(arr11==6):
        arr1.pop()
    arr2.append(arr1.pop())
print(arr2)
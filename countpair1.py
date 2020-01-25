def printPair(arr,arr_size,sum):
    s=set()
    for i in range(0,arr_size):
        temp=sum-arr[i]
        if (temp in s):
            print("pair with given sum"+"is("+str(arr[i])+","+str(temp)+","+")")
        s.add(arr[i])

arr=[1,2,3,4,5,6,7,8]
n=13
printPair(arr,len(arr),n)

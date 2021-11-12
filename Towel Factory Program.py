def tf(N):
    arr=[1,4,9,16]
    op=0
    while N>0:
        for i in range(len(arr)):
            if arr[i]>N or i==(len(arr)-1):
                s=N
                s-=arr[i]
                if s<0:
                    N-=arr[i-1]
                    op+=1
                    break
                N-=arr[i]
                op+=1
                break
            elif arr[i]==N:
                N-=arr[i]
                op+=1
                break
            else:
                pass
    return op
N=int(input().strip())
print(tf(N))

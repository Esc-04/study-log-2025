

print(range(0))
nums = [[num for num in range(n,n+3)] for n in range(1,10,3)] 
result=[[even for even in num if even%2==0] for num in nums]
print(result)

def centerhigh():
    num=map(int,input().split())
    center_num=0
    count=0
    past=next(num)
    present=next(num)

    for future in num:
        if past<present:
            count+=1
        if count>=1:
            if past <= present > future:
                center_num += 1
        past, present = present, future
    return center_num

print(centerhigh())
#이진 탐색은 항상 자료가 정렬되어있을때 사용한다!
#마치 사전같이 

*data,="1,sdofnfwlek"
print(data)

def Binary(data,target,start=0,end=len(data)):
    mid=start+end//2
    
    if start>end:
        return -1
    if data[mid]==target:
        return mid
    elif data[mid]<target:
        start=mid+1
    else: end=mid

    return Binary(data,target,start,end)

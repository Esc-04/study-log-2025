#소사고 알고리즘적 사고의 기초

*data,=1,3,2,5,5,7,3,8,9,0
def LineRecursive(data,num,start,end):
    if start>end:
        return -1
    if data[start]==num:
        return start
    elif data[end]==num:
        return end
    return LineRecursive(data,num,start+1,end-1)

idx=LineRecursive(data,10)

print(idx,data[idx] if idx!=-1 else "")
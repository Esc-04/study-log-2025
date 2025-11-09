#최대 하락 구간길이
def closing():
    d=map(int,input().split())
    next(d)
    status=0
    start=next(d)
    count=0
    maxi=0
    day=0
    bestday=0
    for i,v in enumerate(d,start=2):
        if start>v:
            if status==-1:
                count+=1
                continue
            status=-1
            count+=1
            day=i-1
        elif start<v:
            if status==-1:
                status=1
                if count>maxi:
                    maxi=count
                    bestday=day
        else:
            if status==-1:
                count+=1
        start=v

    if count>maxi:
            maxi=count
            bestday=day
    print(f"최대 하락일 수:{maxi}일 동안 하락\n 최대 하락장 시작날짜: {bestday}일")
        


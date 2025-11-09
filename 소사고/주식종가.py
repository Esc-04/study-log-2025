#주식종가(내힘으로 아자아자!)
#n일 동안 m개의 종목
# stack A stack B stack C
#   1       2       1
#   3       2       5
def closingprice():
    n,m=map(int,input().split())
    data=[[int(x) for x in input().split()] for _ in range(n)]
    for i in range(m):
        count=0
        status=0
        daylong=0
        maxlong=0
        for day in range(n-1):
            priv=data[day][i]
            stack=data[day+1][i]
            if priv<stack:
                if status==1:
                    daylong+=1
                status=1
            elif priv>stack:
                if status==1:
                    count+=1
                    status-=1
                    daylong=0
                    maxlong=max(maxlong,daylong)
            else:
                if status==1:
                    daylong+=1
        maxlong=max(maxlong,daylong)
        if count>=2:
            print(f"{i+1}번째 종목: 주식 종가=[{count}]  최대 상승 구간 길이=[{maxlong}]")

closingprice()




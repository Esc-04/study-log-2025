# 직선간 겹침구간 구하기
def swipline():
    k=int(input())
    data=[tuple(map(int,input().split())) for _ in range(k)]
    count=0
    for i in range(k):
        x,y=data[i]
        for j in range(i+1,k):
            a,b=data[j]
            if x<=a<y or x<=b<y:
                count+=1
    print(count)

#sweep line algorythm

def sweepline():
    #최대 겹침횟수 구하기
    t=int(input())
    base=[tuple(map(int,input().split())) for _ in range(t)]
    events=[]
    for s,e in base:
        events.append((s,1))
        events.append((e,-1))

    events.sort() #정렬하기
    count=0
    maxi=0
    for k,v in events:
        if v==1:
            count+=1
            maxi=max(maxi,count)
        else:
            count-=1

    print(maxi)        

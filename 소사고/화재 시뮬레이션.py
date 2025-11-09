#화재 탈출 시뮬레이션
#n x m 형식의 격자
from collections import deque
def solution():
    def firebfs(x,y): #화재용 bfs
    
        for i,j in zip(dx,dy):
            nx=x+i
            ny=y+j
            if 0<=nx<m and 0<=ny<n: #e단순히 visited True용
                visited[ny][nx]=True
                q.append((nx,ny))


    def humanbfs(x,y):
        for i,j in zip(dx,dy):
            nx=x+i
            ny=y+j
            if (nx==0 or nx==m-1 or ny==0 or ny==n-1) and mapi[ny][nx]=="." and visited[ny][nx]==False:
                    dist[ny][nx]=dist[y][x]+1
                    return dist[ny][nx]
            elif 0<=nx<m and 0<=ny<n and visited[ny][nx]==False and mapi[ny][nx]==".":
                dist[ny][nx]=dist[y][x]+1
                visited[ny][nx]=True
                d.append((nx,ny))
                
    n,m=map(int,input().split())
    mapi=[list(input()) for _ in range(n)]
    visited=[[False] * m for _ in range(n)]
    b,a,d,c=0,0,0,0
    for i in range(n):
        for j in range(m):
            if mapi[i][j]=="S":
                a,b=i,j
            elif mapi[i][j]=="F":
                d,c=i,j
    q=deque([(c,d)]) #화재용 큐
    p=deque([(a,b)]) #생존자 큐
    dist=[[0]*m for _ in range(n)] #거리/시간 계산산
    dist[b][a]=1
    visited[d][c]=True
    visited[b][a]=True

    dx=[0,-1,1,0]
    dy=[-1,0,0,1]


    while p:
        t1=len(q)
        for _ in range(t1):
            x,y=q.popleft() 
            firebfs(x,y) #화재 먼저 확산
        t2=len(p)
        for _ in range(t2):
            a,b=p.popleft()
            status=humanbfs(a,b)
            if status:
                break
    return status if status else 0
   
time=solution()
if time:
    print(time)
else:
    print("impossible")
from collections import deque
import sys
def solution():
    m,n=map(int,sys.stdin.readline().split())
    malp=[list(sys.stdin.readline().strip()) for _ in range(n)]
    dx=[0,-1,1,0]
    dy=[-1,0,0,1]
    visited=[[True if malp[i][j]=="+" else False for j in range(m)] for i in range(n)]
    res={}
    id=1
    def bfs(x,y,id):
        d=deque()
        d.append((x,y))
        count=1
        while d:
            x,y=d.popleft()
            visited[y][x]=True
            for a,b in zip(dx,dy):
                nx=a+x
                ny=b+y
                if 0<=nx<m and 0<=ny<n and visited[ny][nx]==False:
                    count+=1
                    visited[ny][nx]=True
                    d.append((nx,ny))
        res[id]=count
        
    for i in range(n):
        for j in range(m):
            if malp[i][j]=="." and visited[i][j]==False:
                bfs(j,i,id)
                id+=1
    print(len(res))
    print(*sorted(res.values(),reverse=True))
                    
if __name__=="__main__":
    t=int(sys.stdin.readline())
    for _ in range(t):
        solution()
    
#

def solution():
    n,m=map(int,input().split())
    mapi=[list(input().strip()) for _ in range(n)]
    a,b=map(int,input().split())
    dx=[0,-1,-1,0]
    dy=[-1,0,0,1]
    visited=[[False for _ in range(m)] for _ in range(n)]
    count=0
    def dfs(x,y):
            nonlocal count
            visited[y][x]=True
            if mapi[y][x]=="E":
                count+=1
                visited[y][x]=False
                return
            for i,j in zip(dx,dy):
                nx,ny=x+i,y+j
                if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and mapi[ny][nx]==".":
                    dfs(nx,ny)
            visited[y][x]=False

    
    dfs(a,b)
    print(count)
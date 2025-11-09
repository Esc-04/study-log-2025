#정수 n이 주어진다 nxn의 matrix를 만들어보자
#그 후 주,부대각선을 서로 반전시킨다.
from copy import deepcopy
def solution1():
    n=int(input())
    mat=[input().split() for _ in range(n)]
    mat_c=deepcopy(mat)
    for i in range(n):

        mat_c[i][i]=mat[i][n-i-1]
        mat_c[i][n-i-1]=mat[i][i]

    for m in mat_c:
        print(*m)

#크기가 \(N \times N\)인 정수 행렬 `B`가 주어질 때, 이 행렬을 **시계 방향으로 90도 회전**한 결과를 출력하라.
def solution():
    m,n=map(int, input().split())
    mat=[input().split() for _ in range(m)]
    res=[[mat[m-i-1][j] for i in range(m)] for j in range(n)]

    for m in res:
        print(*m)

# **문제 설명**  
# 크기가 \(N \times M\)인 정수 행렬 `C`를 다음 두 가지 방식으로 뒤집어 보자.

# 1. **좌우 반전(Flip Horizontally)**: 각 행에서 오른쪽 열이 왼쪽 열로 바뀌도록 뒤집기  
# 2. **상하 반전(Flip Vertically)**: 각 열에서 아래쪽 행이 위쪽 행으로 바뀌도록 뒤집기  

# 행렬을 입력받고, **먼저 좌우 반전된 결과**, 이어서 **상하 반전된 결과**를 출력하라.

def solution3():
    n,m=map(int,input().split())
    mat=[input().split() for _ in range(n)]

    #좌우 반전
    res1=[[mat[i][n-j-1] for j in range(m)] for i in range(n)]
    #상하 반전
    res=[[mat[m-1-i][j] for j in range(m)] for i in range(n)]

#행렬 덧셈(내힘으로 풀기!)
import 행렬뺄셈 
def matrix(mat1,mat2):
    row=len(mat1)
    col=len(mat1[0])
    res=[[mat1[i][j]+mat2[i][j] for j in range(col)] for i in range(row)]
    return res


n,m=map(int,input().split())
mat1=[[int(x) for x in input().split()] for _ in range(n)]
mat2=[[int(x) for x in input().split()] for _ in range(n)]
res1=matrix(mat1,mat2)
res2=행렬뺄셈.matrix_sub(mat1,mat2)
result=행렬뺄셈.matrix_sub(res1,res2)

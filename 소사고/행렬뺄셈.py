#오늘 행렬 덧셈,뺄셈 기출문제만 풀고 그다음 소프트웨어로 넘어가자!
def matrix_sub(mat1,mat2):
    row=len(mat1)
    col=len(mat1[0])
    result=[[mat1[i][j]-mat2[i][j] for j in range(col)] for i in range(row)]
    return result
#행렬곱셈 sum 인환이 방식으로 풀어보기!

def matrix():
    r,s,t=map(int,input().split())
    mat1=[list(map(int,input().split())) for _ in range(r)]
    mat2=[list(map(int,input().split())) for _ in range(s)]

    total=[[sum(a*b for a,b in zip(i,j)) for j in zip(*mat2)] for i in mat1]
    max=total[0][0]
    min=total[0][0]
    for row in total:
        for c in row:
            if c>max:
                max=c
            if c<min:
                min=c
    return total,max,min
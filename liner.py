# 1학년 2학기 선형대수 1차 과제 : 연립방정식의 해 구하기
# 나의 계획
# 1단계 : 방정식 부분과 상수항 벡터를 따로 받는다
# 2단계 : 행렬식을 구해 det(A)=0 판별로 유일해인지 판단
# 3단계 : 유일해 일 경우 LU분해
# 4단계 : 나머지 경우는 행렬을 가우스-조던 소거법으로 진행
# 5단계 : 자유변수로 무수히 많은 해 표현하기
import sys
#소숫점 이쁘게 표현
def fmt(num):
    if abs(num - int(num)) < 1e-9:
        return str(int(num))
    else:
        return f"{num:.3f}"
    
#2단계
def det(A):     #3x3 행렬식 구하기
    res=0
    for i in range(3):
        mat=[]
        for j in range(3):
            if i!=j:
                mat.append(A[1][j])
                mat.append(A[2][j])
        res+=(-1)**i*A[0][i]*(mat[3]*mat[0]-mat[1]*mat[2])
    return res

#5단계
def gauss(A):
    # 열단위로 소거
    # c는 피벗이 있어야할 행
    for c in range(3):
        for row in range(c,3):
            if A[row][c]!=0:
                pivot=A[row][c]
                n=row #n행으로 갈 인덱스 저장 (행교환에 쓰일것)
                break
        else: #현재 열에는 피벗이 없으므로 contiinue
            continue
        A[c],A[n]=A[n],A[c] #행교환
        A[c]=[num/pivot for num in A[c]] #피벗을 1로 만들기
        
        # c 현재 열
        for row in range(3):
            if row!=c and A[row][c]!=0: #현재 행이거나 0일경우 빼고 연산
                k=A[row][c]
                for j in range(4):      #기본행 연산
                    A[row][j]-=k*A[c][j]

    #해 없음 판단
    for a in A:
        if not any(a[:3]) and a[3]!=0:
            print("해가 없습니다")
            break
    #무수히 많은 해
    else:
        print("무수히 많은 해를 가집니다.")
        return True
    return False
        

#1단계
def solve_matrix():
    print("연립방정식의 계수 부분만 한줄 씩 입력해주세요") 
    print("예시 >>\n1 2 3\n4 5 6\n7 8 9")
    A=[[int(x) for x in sys.stdin.readline().split()] for _ in range(3)]
    print("상수항 3개를 한줄에 입력해주세요") 
    print("예시 >> 1 2 5")
    b=[int(x) for x in sys.stdin.readline().split()]

    #3단계
    if det(A):
        L=[[0]*3 for _ in range(3)]
        U=[[0]*3 for _ in range(3)]
        for t in range(3): #L의 주대각선 1로 초기화
            L[t][t]=1
        for i in range(3):
            for j in range(3):
                total=0
                if i<=j: #U일때
                    for k in range(i):
                        total+=L[i][k]*U[k][j]
                    U[i][j]=A[i][j]-total
                else: #L일때
                    for k in range(j):
                        total+=L[i][k]*U[k][j]
                    L[i][j]=(A[i][j]-total)/U[j][j]

        #Ly=b
        c1=b[0]
        c2=b[1]-L[1][0]*c1
        c3=b[2]-L[2][0]*c1-L[2][1]*c2
        y=[c1,c2,c3]
        #Ux=y
        t3=y[2]/U[2][2]
        t2=(y[1]-U[1][2]*t3)/U[1][1]
        t1=(y[0]-U[0][1]*t2-U[0][2]*t3)/U[0][0]
        
        print(f"해: x={fmt(t1)}, y={fmt(t2)}, z={fmt(t3)}")
    
    #4단계
    else:
        #첨가행렬
        A=[A[i]+[b[i]] for i in range(3)]
        if gauss(A): #무수히 많은  해를 가진다면
            pivot_cols = []
            for r in range(3):
                for c in range(3):
                    # 행 전체가 0이 아니고, c열 값이 1이고 그 왼쪽은 다 0이면 피벗
                    if A[r][c] == 1 and all(A[r][k] == 0 for k in range(c)):
                        pivot_cols.append(c)
                        break
            free_cols = [i for i in range(3) if i not in pivot_cols]
            ans=[0,0,0]
            for f in free_cols:
                ans[f]=chr(ord('s')+f)
            for row in range(3):
                for col in range(3):
                    if col in pivot_cols and A[row][col]==1:
                        ex=str(A[row][3]) #일단 상수항
                        for f in free_cols:
                            if A[row][f]==1:
                                ex+=f"-{ans[f]}"
                            elif A[row][f]==-1:
                                ex+=f"+{ans[f]}"
                            elif A[row][f]==0:
                                continue
                            else:
                                ex+=f"{-A[row][f]}{ans[f]}"
                        ans[col]=ex
            print(f"x={fmt(ans[0])} y={fmt(ans[1])} z={fmt(ans[2])}")



print("과제를 몇번 테스트 하시겠습니까?")
t=int(sys.stdin.readline())
for _ in range(t):
    solve_matrix()




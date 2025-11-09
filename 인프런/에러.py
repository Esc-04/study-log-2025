name= ["조은서","이순남","조성웅"]
# try:
#     print(name[4])

# except IndexError:
#     print("범위 밖입니다")

# finally:
#     print("프로그램을 종료합니다")

#예외 2
while(True):
    try:
        a=input()
        if a=="Cho":
            print("ok")
        else: raise ValueError(f"{a}는 계정 주인이 아닙니다.")
    except ValueError as e:
        print("오류발생 !: ",e)

    else:
        print("은서의 공간에 어서오세요 :)")
        break
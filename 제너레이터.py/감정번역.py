#보람이와 함께하는 감정 번역(데코레이션+예외처리)
import time
def timer(func):
    def wrapper(*args,**kw):
        start=time.time()
        print("함수 호출 시작!✅")
        result =func(*args,**kw)
        end=time.time()
        print(f"최종 실행시간: {end-start:.2f}초")
        return result
        boram.original
    return wrapper

def deco(func):
    def wrapper(*args,**kw):
        print("로그 불러오는 중...🔥")
        result=func(*args,**kw)
        return result
    return wrapper


@timer
@deco
def boram():
    logs=[]
    while(True):
        try:
            feelings=yield
            logs.append(feelings)
            if feelings in ["기쁨","행복","사랑"]:
                print("😊 보람이도 행복해~")
            elif feelings in ["슬픔","우울","속상"]:
                print("😢 보람이가 너를 꼭 안아줄게.")
            elif feelings in ["화남","짜증","스트레스"]:
                print("😠 보람이가 대신 화내줄게!")
            elif feelings == "종료":
                print("실습 끝! 오늘 공부도 알찼어 :)")
                return tuple(logs)
            else:
                raise ValueError("❓ 무슨 감정인지 모르겠어...")
        except ValueError as e:
            print("보람이 당황! ",e)

g=boram()
next(g)
while True:
    message=input("기분이 어때?? ")
    try:
        g.send(message)
    except StopIteration as e:
        print("[System] :",e)
        break


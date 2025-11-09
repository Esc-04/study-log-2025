#고난도 헬퍼함수문제
def deco(func):
    def wrapper(*args,**kwargs):
        print("함수 호출 전! 로딩중..")
        result=func(*args,**kwargs)
        print("로딩 완료! 결과 도출")
        return result
    return wrapper

@deco
def make_deco(symbol):
    def koi(word):
        return f"{symbol}{word}{symbol}"
    return koi

star_wrapper = make_deco('*')("공부집중타임")
print(star_wrapper)
odd_nums = [1, 3, 5, 7, 9]
c=odd_nums
b=c.copy()
print(id(b))
def add_odds(odds):
    print(id(odds))
    odds+=[1,2]
    print(odds) 

add_odds(b)


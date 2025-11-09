#문자 포장기 함수 공장
import inspect
def make_decorator(t):
    print("Path: "+inspect.getfile(inspect.currentframe()))
    def deco(w):
        return f"{t}{w}{t}"
    return deco

if __name__=="__main__":
    make_star=make_decorator("🎀")
    make_heart=make_decorator("💖")
    print(make_star("은서"))
    print(make_heart("보람"))
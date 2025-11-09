#해시값으로 비교
#🍱 실습 주제: MenuItem 클래스 만들기
# 요구사항

# 속성: name(이름), calories(칼로리)

# __hash__()는 name을 기준으로 만들기

# __eq__()는 name이 같으면 같다고 처리

# set()에 메뉴 여러 개 넣어보고, 중복 없이 관리되는지 확인해보기!

class MenuItem():
    def __init__(self,name,cal):
        self._name=name
        self._cal=cal

    def __hash__(self):
        return hash(self._name)
    
    def __eq__(self,other):
        return self._name==other._name
    
    def __str__(self):
        return f"이름:{self._name}/ 칼로리: {self._cal}kcal"
    


food_set=set()
a=MenuItem("라떼",175)
b=MenuItem("초밥",200)
c=MenuItem("초밥",300)
d=MenuItem("스테이크",200)
food_set.update([a,b,c,d])
print(*food_set)


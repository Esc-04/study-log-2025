#매직 메서드1
class Fruit:
    """
    <과일 클래스> :이름 , 가격
    """
    def __init__(self,name,price):
        self.__name=name
        self.__price=price


#===== 접근자와 설정자 =================================       
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def delName(self):
        print("이름 삭제 중..")
        self.__name="알 수 없음"

    name=property(getName,setName,delName," 과일의 이름을 나타내며며 private입니다.")
#=======================================================

    def __add__(self,x):
        return self._price-x.__price
    
    def __le__(self,x):
        return self.__price<=x.__price
    
    def __eq__(self, value):
        return self.__price%10==0 and value.__price%10==0
    
f1=Fruit("orange",1500)
f2=Fruit("apple",800)
help(Fruit.name)

print(10/10)
#클래스 기초
# 자동차 공장을 클래스로 설계하고,
# 생성된 자동차들의 수를 추적하고,
# 각 자동차가 만들어질 때마다 일련번호(serial number)를 부여하며,
# 이름, 연식은 수정할 수 없고, 주행 거리(km)는 setter를 통해 검증된 값만 수정 가능해야 한다

class CarFactory():
    """
    코딩 2개월차 국민대 python 공부 중 만들어보는 자동차 공장
    private과 getter/setter @property 사용
    오늘 새롭게 배운것: 메서드도 private이 가능하다는것
    del 함수에 print("삭제")를 하면 알수있듯 인터프리터가 끝나면 class 에서 생성된 객체는 모두 삭제된다!
    알게모르게... del class자체를 하면 마지막에 삭제할 객체들이 참조할게 없어지니 오류가 나게된다
    """
    __carNum=0
    
    def __init__(self,model,year,distance):
        if CarFactory.__isOk(model):
            raise ValueError(f"{model}은 이름으로 사용할 수 없습니다.")
        if distance<0:
            raise ValueError("주행거리는 음수가 될 수 없습니다")
        #raise를 했으니 따로 else 불필요
        self.__model=model
        self.__year=year
        self.__distance=distance
        self.__serial_number=CarFactory.__carNum+2025 #현재 년도부터 시리얼 넘버버
        CarFactory.__carNum+=1
    def __str__(self):
        return f"이 자동차의 시리얼 넘버는 {{{self.__serial_number}}}입니다"
    
    def __repr__(self):
        return f"CarFactory(model={self.__model!r},year={self.__year+1!r},distance={self.__distance!r})"
    def getmodel(self):
        return self.__model
    def getyear(self):
        return self.__year
    
    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self,length):
        if length<0:
            print("[System] 주행 거리는 0 이상")
        else:
            self.__distance=length
    @classmethod
    def show_status(cls):
        print(f"현재 차량의 수 = {cls.__carNum}대")
    @staticmethod
    def __isOk(name):
        return bool(not name or name.isspace() or name.isdigit())
    def __del__(self):
        model=getattr(self,"_CarFactory__model","미정")
        print(f"[{model}] 차량이 폐기 되었습니다.")
        if CarFactory.__carNum!=0:
            CarFactory.__carNum-=1
        

try:
    car1=CarFactory("123",2025,1)
except ValueError as e:
    print('오류 발생!:',e)
twin=CarFactory("쌍둥이차",1,100)
twins=eval(repr(twin))
print(twin)
print(twins)
twin.distance(20)
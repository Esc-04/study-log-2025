# 생성자 __init__()에서 아래 값을 받는다:
# 모델명 model (예: "제네시스")
# 연식 year (예: 2022)
# 초기 주행거리 distance (기본값은 0km)
# 다음과 같은 메서드를 만든다
# drive(km) : distance를 km만큼 증가시키고 "주행 중... 총 주행거리 Xkm" 출력
# get_info() : "모델: OOO | 연식: YYYY | 주행거리: ZZZkm" 출력
# reset_distance() : distance를 0으로 초기화하고 "주행 기록이 초기화되었습니다." 출력
# 클래스 변수 total_cars를 만들어, 생성될 때마다 1씩 증가
# 클래스 메서드 show_total()을 만들어 "총 등록된 차량 수: N대"를 출력


class Car:
    __car_set=[]
    total_car=0
    @classmethod
    def show_total(cls):
        print("총 등록된 차량 수:",Car.total_car,"대")

    @classmethod
    def carList(cls):
        return list(Car.__car_set)
    def __init__(self,model,year,distance=0):
        self.model=model
        self.year=year
        self.distance=distance
        Car.__car_set.append(self.model)
        Car.total_car+=1
        print("차량 등록 완료되었습니다.")



    #del 함수의 주의할점!
    #인터프리터가 끝나는 시점에 python은 자동으로 생성된 모든 객체를 삭제한다 
    #마지막에 삭제되었습니다가 2번 호출되는 이유는 car1과 car3이 자동 삭제되기때문이다
    #del을 쓰면 우리가 강제로 먼저 삭제하는 것! (의도적인)

    def __del__(self):
        print(f"[System] {self.model}삭제 완료!")
        Car.__car_set.remove(self.model)
        Car.total_car-=1
        

    def __str__(self):
        return f"이 차량의 모델은 [{self.model}]입니다"
    
    def drive(self,km):
        self.distance+=km
        print(f"주행 중... 총 {self.distance}km")

    def get_info(self):
        return f"모델: {self.model} | 연식: {self.year} | 주행거리: {self.distance}"
    def reset_distance(self):
        self.distance=0
        print("주행 거리가 초기화되었습니다")

jeneciss=Car("제네시스",2002,10)
santa=Car("산타페",1995,15)    
morning=Car("모닝",2015,17)
del jeneciss
del santa
del morning
del Car

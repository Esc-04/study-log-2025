# 💼 설정
# Employee: 모든 직원의 공통 클래스
# 이름(_name)과 사번(__id)은 private으로

# get_info() 메서드 존재 (접근자 사용

# Developer: Employee 상속

# 기술스택(__stack)은 private
# 오버라이딩된 get_info()는 name, id, stack 모두 출력
# Manager: Employee 상속
# __team (비공개 리스트)
# 팀원 추가 메서드: add_member()
# Developer만 받아야 함 (아닐 경우 거절 메시지 출력)
# 내부에 getter 사용해서 name만 출력 가능

class Employee():
    total=0
    def __init__(self,name,id):
        self.__name=name
        self.__id=id
        Employee.total+=1

    def get_info(self):
        return f"이름:{self.__name} / 사번:{self.__id}"
    
class Developer(Employee):
    def __init__(self,name,id,stack):
        super().__init__(name,id)
        self.__stack=stack

    def get_info(self):
        info=super().get_info()+f"학습언어: [{self.__stack}]"

        return info
    
class Manager(Employee):
    def __init__(self,name,id):
        super().__init__(name,id)
        self.__team=[]
    def add_member(self,dev):
        if isinstance(dev,Developer):
            self.__team.append(dev)
        else:
            print("Dont' access")
    def getName(self):
        print(self.__name)
    def get_info(self):
        info=f"""{super().get_info()}\n"""
        for i in self.__team:
            info+=f" -{i.get_info}"
        return info
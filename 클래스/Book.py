#도서관 시스템
import time
class Book:
    __total_book=[]
    def __init__(self,name,val):
        self.name=name
        self.__val=val
        Book.__total_book.append(self.name)
        self.__borrow=False
    def getborrow(self):
        return "책을 빌림" if self.__borrow else "빌리지 않음"
    def getVal(self):
        return self.__val
    def setVal(self,val):
        self.__val=val
    def delVal(self):
        print(self.name,"책 등록을 삭제합니다.")
        Book.__total_book.remove(self.name)

    val=property(getVal,setVal,delVal,"책의 가격 변수입니다.")

    @classmethod
    def gettotalBook(cls):
        return cls.__total_book
    
    def __str__(self):
        return f"책 제목: {self.name}  -  가격:{self.__val}"
    
    def __eq__(self, other):
        return self.name==other.name
    
    def __hash__(self):
        return hash(self.name)
    
    def __ne__(self, value):
        return self.name!=value.name
    
    @staticmethod
    def hello():
        print("📖 Welcome to the ESC's Library System!")

    def borrow(self):
        self.__borrow=True
        print(self.name,"책을 대여합니다.")
        self.__start=time.perf_counter()
    def return_book(self):
        self.__borrow=False
        print(self.name,"책을 반납하였습니다.")    
        self.__end=time.perf_counter()
        print(self.__end-self.__start,"동안 책을 빌렸습니다")

b1=Book("Python 마스터",24000)
b2=Book("객체지향 입문",12000)
b3=Book("C++ 기초 다지기",78000)
b4=Book("알고리즘 기초",30000)
b4.borrow()
print(Book.gettotalBook())
print("두 책은 같습니다" if b2==b3 else "같은 책이 아닙니다.")
for i in Book.gettotalBook():
    print(i)
time.sleep(10)
print(b3.__dict__)
print(type(b1).__name__)
b4.return_book()



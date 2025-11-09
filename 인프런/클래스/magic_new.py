#문자열을 살아있게 바꿔보자!
class Special(str):
    def __new__(cls,name):
        return super().__new__(cls,name)
    
mystring=Special("은서")
print(mystring)
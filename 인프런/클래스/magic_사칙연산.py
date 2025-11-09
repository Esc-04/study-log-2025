
class MysteryBox():
    def __init__(self,number):
        self.__number=number

    def getnumber(self):
        return self.__number

    def __add__(self,other):
        return MysteryBox(self.__number+other.getnumber())
    
    def __radd__(self,other):
        return MysteryBox(self.__number+other)
    
    def __itruediv__(self,other):
        return MysteryBox(self.__number/other.getnumber())
    
    def __floordiv__(self,other):
        return MysteryBox(self.__number//other.getnumber())
    
    def __iadd__(self,other):
        self.__number+=other.getnumber()
        return MysteryBox(self.__number)
    
    def __mod__(self,other):
        return MysteryBox(self.__number%other.getnumber())
    
    def __repr__(self):
        return f"📦 {self.__number}"

a = MysteryBox(10)
b = MysteryBox(3)

print(a + b)      # 📦 13
print(5 + b)      # 📦 8
print(a // b)     # 📦 3
print(a % b)      # 📦 1

a += b
print(a)          # 📦 13

    

#벡터 클래스

class Vector(object):
    def __init__(self,*args):
        """
        Create Vector ,example v=Vector(5,10)
        """
        if len(args)!=2:
            raise ValueError (args)
        else:
            self._x,self._y=args
    def __repr__(self):
        """
        Return the vector info
        """
        return "Vector(%r,%r)" % (self._x,self._y)
    
    def __add__(self,other):
        """
        Return the addition of two Vector
        """
        return Vector(self._x+other._x,self._y+other._y)
    
    def __mul__(self,other):
        """
        Return the multiply of two Vecotr
        """
        return Vector(self._x*other,self._y*other)
    def __radd__(self,other):
        if other==0:
            return self
        #else:self.__add__(other)
    
    def __bool__(self):
        """
        is basepoint
        """
        return not bool(max(self._x,self._y))
    

def V_addition():
    isAcceptable=True
    box=[]
    while(isAcceptable):
        try:
            v=Vector(*map(int,input().split()))
            box.append(v)
            if len(box)==3:
                isAcceptable=False
        except ValueError as e:
            print("2개의 인자를 채워주세요:",e)
    new_v=sum(box)
    print(new_v)

    if (input("Try Again? Y/N")) in ["Y","y"]:
        V_addition()
V_addition()
print(Vector.__bool__.__doc__)
print(Vector.__add__.__doc__)

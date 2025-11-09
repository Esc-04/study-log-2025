import traceback
def myfunc(val):
    if val==0:
        raise Exception("no zero!!")
    elif val<0:
        raise Exception("no minus!!")
    

class NoNegative(Exception):
    def __init__(self,msg="should not be a negative!!"):
        super().__init__(msg)
        self.msg=msg
 

class Zerocola(Exception):
    pass

def myfunc2(val):
    if val==0:
        raise Zerocola()
    elif val<0:
        raise NoNegative(val)
    
try:
    value=0
    myfunc2(value)
except (NoNegative,Zerocola) as e:
    print(e)
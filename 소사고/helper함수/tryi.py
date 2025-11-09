
import traceback
def double():
    def mini():
        try:
            a=[1,2,3]
            try:
                a.remove(50)
            except ValueError:
                raise
        except ValueError:
            raise
    try:
        mini()
    except:
        traceback.print_exc()
try:
    double()
except ValueError as e:
    traceback.print_exc()
import datetime
import time
class Aplusb:
    @classmethod
    def _a(cls,a,b,**kwargs):
        c = datetime.datetime.now()
        return a+b,c
sum ,time1 = Aplusb._a(1,2)
print(sum,time1)
time.sleep(2)
sum,time2 = Aplusb._a(3,4)
print(sum,time2)

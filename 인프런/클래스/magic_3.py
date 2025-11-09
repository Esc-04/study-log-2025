#네임드 튜플, 데이터 전처리
pt1=(1.0,5.0)
pt2=(2.5,1.5)
from math import sqrt
len1=sqrt((pt2[0]-pt1[0])**2+(pt1[1]-pt2[1])**2)

from collections import namedtuple
#네임드 튜플 선언!
Point=namedtuple('Point',"x y")
pt3=Point(1.0,5.0)
pt4=Point(2.5,1.5)
print(pt3)

len2=sqrt((pt3.x-pt4.x)**2+(pt3.y-pt4.y)**2)
print(Point)

#실 사용 사례
Class =namedtuple("Class","rank number")
#그룹 리스트 선언
numbers=[x for x in range(1,21)]
ranks="A B C D".split()
students=[Class(a,b) for a in ranks for b in numbers]
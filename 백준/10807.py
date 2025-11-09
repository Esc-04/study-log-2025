import sys
c=input()
count=list(map(int,(sys.stdin.readline().split())))
base=int(sys.stdin.readline())
com=0
for i in count:
    if i==base:
        com+=1
print(com)
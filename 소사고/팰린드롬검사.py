def checksum():
    origin=bin(int(input()))[2:].zfill(32)
    st=[]
    for i in range(0,30,8):
        st.append(origin[i:i+8])
        
    chk=sum(map(int,st[:3]))
    while chk>=256:
            chk-=256
    if int(st[3])==255-chk:
        print(1)
    else:
        print(0)
        
t=int(input())
for _ in range(t):
    checksum()
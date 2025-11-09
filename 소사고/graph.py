def graph():
    origin=int(input())
    k=origin//2
    for i in range(origin):
        gpl=""
        for j in range(origin):
            if i==k and j==k:
                gpl+="O"
            elif i==k:
                gpl+="+"
            elif j==k:
                gpl+="I"
            elif j==origin-1-i:
                gpl+="*"
            else:
                gpl+="."
        print(gpl)
            

def graph2():
    origin=int(input())
    kl=(origin-1)//2
    kr=origin//2
    for i in range(origin):
        gpl=""
        for j in range(origin):
            if i==origin//2:
                kl=origin-1
                kr=0
            if j==kl:
                gpl+="/"
            elif j==kr:
                gpl+="\\"
            elif kl<j<kr or kr<j<kl:
                gpl+="x"
            else:
                gpl+="."
        kr+=1
        kl-=1
        print(gpl)
graph2()

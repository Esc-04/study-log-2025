import sys
def checksum():
    origin=bin(int(sys.stdin.readline()))[2:].zfill(32)
    data=[]
    for i in range(0,len(origin),8):
        data.append(int(origin[i:i+8],2))

    dataset=sum(data[:3])
    while dataset>=256:
        dataset-=256
        
    print(0 if 255-dataset!=data[3] else 1)
    
def testcase():
    t=int(sys.stdin.readline())
    for _ in range(t):
        checksum()
        
if __name__=="__main__":
    testcase()
    
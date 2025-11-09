


def printgraph(k):
    cen=k//2
    graph_list=[["." for _ in range(k)] for _ in range(k)]
    for i in range(k):
        graph_list[i][k-i-1]="*"
        graph_list[i][cen]="I"
    graph_list[cen]=["+" for _ in range(k)]
    graph_list[cen][cen]="O"

    for j in range(k):
        print("".join(graph_list[j]))

def testCase():
    test=int(input())
    for _ in range(test):
        num=int(input())
        printgraph(num)
    
testCase()
print(__name__)
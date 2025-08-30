# 수 찾기 실버4
n1 = int(input())
li1 = list(map(int, input().split()))
n2 = int(input())
li2 = list(map(int, input().split()))

for i in li2:
    if i in li1:
        print(1)
    else:
        print(0)
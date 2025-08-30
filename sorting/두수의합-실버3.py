# 😇 두 수의 합 실버3 
# 처음 실패 시간복잡도를 고려하지 않고 n^2으로 해서 그런듯.
import sys

n = int(input())

li = list(map(int, sys.stdin.readline().split()))

found = int(input())

cnt = 0

for i in range(n-1):
    for j in range(i+1, n):
        if li[i] + li[j] == found:
            cnt += 1

print(cnt)

'''
#시간 복잡도를 n log(n)으로 수정한 방법. 전제가 모두 서로 다른 양수이기에 가능한 코드.
import sys

n = int(input())
li = list(map(int, sys.stdin.readline().split()))
x = int(input())

cnt = 0
start = 0
end = len(li)-1

li.sort()

while start < end:
    if li[start] + li[end] == x:
        cnt += 1
        start += 1
        end -= 1
    elif li[start] + li[end] < x:
        start += 1
    else :
        end -= 1

print(li)
'''
# 먹을 것인가 먹힐 것인가 실버3
import sys
import bisect

testcase_n = int(input())

for i in range(testcase_n):
    n, m = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    A.sort()
    B.sort()
    B_MAX = max(B)
    cnt = 0

    for A_num in A:
        if A_num > B_MAX:
            cnt += len(B)
        else:
            cnt += bisect.bisect_left(B, A_num)

    print(cnt)

                
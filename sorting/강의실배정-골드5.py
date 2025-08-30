# 강의실 배정 골드 5
# 전에 그리드랑 거의 같다. 까먹을 때쯤 한 번 더 풀어보자.
import sys
import heapq

n = int(input())
li = [list(map(int,sys.stdin.readline().split())) for i in range(n)]

def max_classtime(li):
    li.sort(key = lambda x: x[1])

    cnt = 0
    end_time = -1

    for start, end in li:
        if start >= end_time:
            cnt += 1
            end_time = end

    return cnt 


print(max_classtime(li))
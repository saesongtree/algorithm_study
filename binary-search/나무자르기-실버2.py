# 나무 자르기 실버2
# 시간 초과남
import sys

tree_cnt, req_tree = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

h = max(tree) - 1
sum = 0

while sum < req_tree:
    for tree_h in tree:       
        if tree_h > h:
            sum += tree_h - h
    if sum >= req_tree:
        break
    else:
        h -= 1
        sum = 0        
    

print(h)



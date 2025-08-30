# 소트인사이드 실버5

n = input()
arr = []

for i in range(len(n)):
    arr.append(n[i])

arr.sort(reverse = True)
for i in range(len(n)):
    print(arr[i],end='')
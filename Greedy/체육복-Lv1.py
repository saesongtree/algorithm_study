def solution(n, lost, reserve):

    answer = 0

    arr = [1]*n #배열 크기 n

    for j in lost: #도난 당한 학생은 0
        arr[j-1] -= 1

    for k in reserve: #여유분 있으면 2
        arr[k-1] += 1

    for i in range(n):
        if arr[i] == 0:
            if i > 0 and arr[i-1] > 1: #왼쪽 확인
                arr[i-1] -= 1
                arr[i] += 1
            elif i < n-1 and arr[i+1] > 1: #오른쪽 확인
                arr[i+1] -= 1
                arr[i] += 1
    for a in range(n):
        if arr[a] > 0:
            answer += 1
            
    return answer

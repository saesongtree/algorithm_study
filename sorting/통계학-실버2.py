# 통계학 실버2
import sys

N = int(sys.stdin.readline())
number = [int(sys.stdin.readline()) for i in range(N)]

number.sort()

'''def avg_result(arr):
    start = 0
    end = len(arr) - 1 
    sum = 0
    while start < end:
        sum += arr[start] + arr[end]
        start += 1
        end -= 1
    if start == end:
        sum += arr[start]
    
    return sum'''
# .. total = sum(number) 함수 메소드 좀 쓰자 ... 
# 😫 += 와 = 는 확연하게 다르다. sum = sum + a 랑 sum = a
# 전자는 합산이고 후자는 그냥 재선언이다. 당연해도 확실하게 기억하자.

total = sum(number)
avg = round(total / len(number)) #산술평균값

middle_number = number[int((len(number)-1)/2)] # 중앙값

#len(number)/2가 왜 []에 안 들어갈까? /2하는 순간 파이썬은 float형이다.
#나누기 값 인덱스에 넣으려면 int를 씌우자.

def mode(arr):
    min_value = min(arr)
    max_value = max(arr)
    size = max_value - min_value + 1
    cnt = [0] * size
    
    for num in arr:
        cnt[num - min_value] += 1  # offset 적용
    
    max_count = max(cnt)
    modes = [i for i, count in enumerate(cnt) if count == max_count]
    modes.sort()

    return modes[1] + min_value if len(modes) > 1 else modes[0] + min_value

#인덱스 값에는 음수가 들어갈 수 없기 때문에 보정을 해줘야함.


range = max(number) - min(number)

print(avg)
print(middle_number)
print(mode(number))
print(range)





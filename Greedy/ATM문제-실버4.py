#ATM 문제

def min_time(n, li): 
  
  li.sort() #오름 차순 정리

  sum = 0
  cal_sum = 0

  for i in li:
    sum += i #누적합
    cal_sum += sum #누누적합
  
  return cal_sum

N = int(input())
T = list(map(int, input().split()))

print(min_time(N, T))
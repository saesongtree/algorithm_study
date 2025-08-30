def AtoB(a, b):
  cnt = 0
  
  while a < b:
      if b % 10 == 1:
        b = int(b / 10) #끝자리가 1일 경우 지우기
        cnt += 1
      elif b % 2 == 0: 
        b = (b / 2)
        cnt += 1
      else :
        break

  if b == a :
        cnt += 1
  else :
        cnt = -1

  return cnt
  

num1, num2 = list(map(int, input().split()))
print(AtoB(num1, num2))
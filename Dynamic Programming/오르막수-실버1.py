import sys
N = int(sys.stdin.readline())

# dp[i][j]: 길이가 i이고 마지막 숫자가 j인 오르막 수의 개수
dp = [[0] * 10 for _ in range(N + 1)]

# 길이가 1인 오르막 수는 0~9 모두 1개씩 존재
for i in range(10):
    dp[1][i] = 1

# 길이가 2부터 N까지의 오르막 수를 계산
for i in range(2, N + 1):
    for j in range(10):
        # 마지막 숫자가 j인 오르막 수는
        # 길이가 i-1이고 마지막 숫자가 0부터 j까지인
        # 오르막 수들의 합과 같다.
        for k in range(j + 1):
            dp[i][j] = (dp[i][j] + dp[i-1][k]) % 10007

# 길이가 N인 오르막 수의 총개수는 dp[N][0]부터 dp[N][9]까지의 합
result = sum(dp[N]) % 10007
print(result)
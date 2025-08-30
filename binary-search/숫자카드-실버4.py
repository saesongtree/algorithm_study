# 숫자 카드 실버4
import sys
import bisect

# 카드 개수
N = int(input())
# 가지고 있는 카드 리스트를 정렬
card_list = sorted(map(int, sys.stdin.readline().split()))

# 찾을 숫자 개수
M = int(input())
find_numbers = list(map(int, sys.stdin.readline().split()))

# 이분 탐색으로 존재 여부 확인 함수
def is_exist(target, sorted_list):
    # bisect_left는 이분 탐색을 수행하여 target이 들어갈 위치 반환
    index = bisect.bisect_left(sorted_list, target)
    # 만약 그 위치에 값이 존재하면 1, 아니면 0
    if index < len(sorted_list) and sorted_list[index] == target:
        return '1'
    else:
        return '0'

# 결과 리스트 생성
result = [is_exist(num, card_list) for num in find_numbers]

# 출력
print(' '.join(result))

#bisect.bisect.left(함수, 찾을 값)이거 익숙해지자.

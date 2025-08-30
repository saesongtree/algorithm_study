# 실버 1 신입 사원
import sys
n = int(input())
for i in range(n):
    m = int(input())
    applicants = []

    for i in range(m):
        doc_score, interview_score = map(int, sys.stdin.readline().split())
        applicants.append((doc_score, interview_score))
        

        applicants.sort(key=lambda x: x[0])
    
        count = 0
        min_interview_rank = m + 1
    
        for i, interview_rank in applicants:
            if interview_rank < min_interview_rank:
                count += 1
                min_interview_rank = interview_rank
            
    print(count)
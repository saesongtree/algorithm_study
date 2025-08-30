import heapq

def Need_Room(li):
    li.sort(key = lambda x : x[0])
    end_times = []
    for S, T in li:
        if end_times and end_times[0] <= S:
            heapq.heapreplace(end_times, T)
        else:
            heapq.heappush(end_times, T)
            
    return len(end_times)

classTime = []

N = int(input())
for i in range(N) :
  s, t = map(int, input().split())
  classTime.append((s,t))

print(Need_Room(classTime))

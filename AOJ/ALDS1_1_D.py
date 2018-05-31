n = int(input())

min_rate = 10**15
max_prof = -10**15
for i in range(n):
    rate = int(input())
    prof = rate - min_rate
    if prof > max_prof:
        max_prof = prof
    if min_rate > rate:
        min_rate = rate

print(max_prof)
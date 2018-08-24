# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

idx = 0
for i in range(n):
 if a[i] > a[idx]:
  idx = i
a[idx], a[-1] = a[-1], a[idx]

idx = 0
for i in range(n-1):
 if a[i] > a[idx]:
  idx = i

result = a[idx]*a[-1]

print(result)

n_set = set()
m_set = set()
(n, m) = input().split(' ')
n = int(n)
m = int(m)
for _ in range(n):
    number = (input())
    n_set.add(number)
for _ in range(m):
    number = (input())
    m_set.add(number)
nm_intersect = list(n_set.intersection(m_set))
for i in range(len(nm_intersect)):
    print(nm_intersect[i])

# class UF:
#     def __init__(self, V): # V: the number of vertices
#         self.ids = [] # ids[i]: i's parent
#         self.size = [] # size[i]: size of tree rooted at i
#         for idx in range(V + 1):
#             self.ids.append(idx)
#             self.size.append(1)
#
#     def root(self, i):
#         while i != self.ids[i]: i = self.ids[i]
#         return i
#
#     def connected(self, p, q):
#         return self.root(p) == self.root(q)
#
#     def union(self, p, q):
#         id1, id2 = self.root(p), self.root(q)
#         if id1 == id2: return
#         if self.size[id1] <= self.size[id2]:
#             self.ids[id1] = id2
#             self.size[id2] += self.size[id1]
#         else:
#             self.ids[id2] = id1
#             self.size[id1] += self.size[id2]


import sys

input = sys.stdin.readline


N, M = map(int, input().split())

knowSet = set(input().split()[1:])
parties = []

for _ in range(M):
    parties.append(set(input().split()[1:]))

for _ in range(M):
    for party in parties:
        if party & knowSet:
            knowSet = knowSet.union(party)

ans = 0
for party in parties:
    if party & knowSet:
        continue
    ans += 1
print(ans)
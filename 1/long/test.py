G = input()

G = open(G).readlines()
for i in range(0,len(G)):
  G[i] = G[i].strip('\n').split()

new = []
for i in range(0,len(G)):
  list = []
  for j in range(i, len(G)):
    list.append(G[j-i][j])
  new.append(list)

  list_vert = []
  for j in range(i, len(G)):
    list_vert.append(G[j][j-i])
  new.append(list_vert)

del new[0]
for i in range(0, 4):
  del new[-1]


print(new)
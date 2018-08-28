file = input()
a = open(file).readlines()
for i in range(0, len(a)):
	a[i] = a[i].strip('\n').split()

print(a)
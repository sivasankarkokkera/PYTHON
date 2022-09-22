MAX = 500001
parent = [0] * MAX
Rank = [0] * MAX

def find(x):
	
	if parent[x] == x:
		return x
	else:
		return find(parent[x])
def merge(r1, r2):

	if(r1 != r2):
		if(Rank[r1] > Rank[r2]):
			parent[r2] = r1
			Rank[r1] += Rank[r2]

		else:
			parent[r1] = r2
			Rank[r2] += Rank[r1]

def minimumOperations(s1, s2):
	for i in range(1, 26 + 1):
		parent[i] = i
		Rank[i] = 1
	ans = []
	for i in range(len(s1)):
		if(s1[i] != s2[i]):
			if(find(ord(s1[i]) - 96) !=
			find(ord(s2[i]) - 96)):

				x = find(ord(s1[i]) - 96)
				y = find(ord(s2[i]) - 96)
				merge(x, y)
				ans.append([s1[i], s2[i]])

	print(len(ans))
	for i in ans:
		print(i[0], "->", i[1])
if __name__ == '__main__':
	s1 = "cat"
	s2 = "cut"
	minimumOperations(s1, s2)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms

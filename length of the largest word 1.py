def lengthOfLastWord(a):
	l = 0
	x = a.strip()

	for i in range(len(x)):
		if x[i] == " ":
			l = 0
		else:
			l += 1
	return l
if __name__ == "__main__":
	inp = input("enter the string")

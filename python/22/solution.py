print(ord('A'))

def score_name(name):
	"""
	INPUT: name - a string
	OUTPUT: score - an integer representing the value of the string
	"""
	score = 0
	for char in name:
		score += (ord(char)-64)
	return score


source = open("names.txt", "r")
unparsed = source.read()
names = [name.replace('"', '') for name in unparsed.split(",")]
names.sort()


total_score = 0
for index in range(len(names)):
	total_score += (1+index) * score_name(names[index])

print(total_score)




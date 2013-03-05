# Name: Chris Van Schyndel

# Week 5 Lab

def is_valid_word(letters, word_compare, min_length, total_length):
	# This function takes a string and a dictionary, and finds the possible
	# spelled words based on the max length and min length.
	comparedictone = letters
	comparedicttwo = {}
	# Initialize dictionaries and standardize strings to lower case for comparison
	word_compare = word_compare.lower()
	# Populate dictionaries, if a letter exists, add to it's count value, if not, add it
	# initially with a count value of 1.
	for letter in word_compare:
		if letter in comparedicttwo:
			comparedicttwo[letter] = comparedicttwo[letter] + 1
		else:
			comparedicttwo[letter] = 1
	# Remove empty spaces from dictionaries, as they do not matter for comparison.
	if ' ' in comparedictone:
		del comparedictone[' ']
	if ' ' in comparedicttwo:
		del comparedicttwo[' ']
	lettercount = 0
	comparecount = sum(comparedicttwo.values())
	for letter in letters:
		if letter in comparedicttwo:
			lettercount += 1
			if comparedicttwo[letter] == 1:
				del comparedicttwo[letter]
			else:
				comparedicttwo[letter] = comparedicttwo[letter] - 1
	lettercount = comparecount - lettercount
	if (comparecount - lettercount) >= min_length and comparecount <= total_length:
		return True
	else:
		return False
		

def find_scrabblies(letters, min_length, total_length):
	baglace = open('words.txt')
	wordlist = []
	validlist = []
	for line in baglace:
		word = line.strip()
		wordlist.append(word)
	for word in wordlist:
		if is_valid_word(letters, word, min_length, total_length):
			validlist.append(word)
	return validlist

def letters_to_dict(letters):
	comparedict = {}
	for letter in letters:
		if letter in comparedict:
			comparedict[letter] = comparedict[letter] + 1
		else:
			comparedict[letter] = 1
	return comparedict

			
print find_scrabblies('bagel', 5, 8)
#print is_valid_word(letters_to_dict('lageb'), 'bagelo', 3, 6)


# Name: Chris Van Schyndel

# Exercise 12.4

def is_anagram(stringone, stringtwo):
	# This function takes two strings and returns True or False relative
	# to whether or not they are anagrams of each other.
	comparedictone = {}
	comparedicttwo = {}
	# Initialize dictionaries and standardize strings to lower case for comparison
	stringone = stringone.lower()
	stringtwo = stringtwo.lower()
	# Populate dictionaries, if a letter exists, add to it's count value, if not, add it
	# initially with a count value of 1.
	for letter in stringone:
		if letter in comparedictone:
			comparedictone[letter] = comparedictone[letter] + 1
		else:
			comparedictone[letter] = 1
	for letter in stringtwo:
		if letter in comparedicttwo:
			comparedicttwo[letter] = comparedicttwo[letter] + 1
		else:
			comparedicttwo[letter] = 1
	# Remove empty spaces from dictionaries, as they do not matter for comparison.
	if ' ' in comparedictone:
		del comparedictone[' ']
	if ' ' in comparedicttwo:
		del comparedicttwo[' ']
	# Compare dictionaries, if all keys and values match, then they are anagrams.
	if comparedictone == comparedicttwo:
		keylist = comparedictone.keys()
		keys = ''
		for letter in keylist:
			keys += letter
		return True, keys
	else:
		return False, [' ']

def find_anagrams(filename):
	# Takes a word list from a file and returns all the anagrams contained within.
	baglace = open(filename)
	anagram_dict = {}
	wordlist = []
	for line in baglace:
		word = line.strip()
		wordlist.append(word)
	for word1 in wordlist:
		for word2 in wordlist:
			if word1 != word2:
				tupleholder = is_anagram(word1, word2)
				if tupleholder[0]:
					if tupleholder[1] in anagram_dict:
						if word1 not in anagram_dict[tupleholder[1]]:
							anagram_dict[tupleholder[1]].append(word1)
						if word2 not in anagram_dict[tupleholder[1]]:
							anagram_dict[tupleholder[1]].append(word2)
					else:
						anagram_dict[tupleholder[1]] = [word1, word2]
	return anagram_dict

			

print find_anagrams('wordies.txt')


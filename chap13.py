# Name: Chris Van Schyndel

# Exercise 13.8
import random


def markov_dict_create(filename, order):
	bag = open(filename)
	lines = bag.readlines()
	counter = 1
	counter2 = 0
	markov_dict = {}
	wordlist = []
	for line in lines:
		wordlist += line.split(" ")
	for element in wordlist:
		modulo = order + 1
		if counter % modulo == 0:
			counter = 1
			prefix = ''
			looptemp = order
			for ordercount in range(order):
				prefix += wordlist[counter2-looptemp] + ' '
				looptemp -= 1
			if element in markov_dict:
				markov_dict[prefix] = markov_dict[prefix] + [' ' + element]
			else:
				markov_dict[prefix] = element
		else:
			counter += 1
		counter2 += 1
	return markov_dict

def markov_analysis(markov_dict):
	finalstory = ''
	counter = len(markov_dict)
	listofkeys = []
	antilist = []
	for keys in markov_dict:
		listofkeys.append(keys)
	random.shuffle(listofkeys)
	for key in listofkeys:
		finalstory += str(key) + str(markov_dict[key]) + ' '
	return finalstory


print markov_analysis(markov_dict_create('dogsong.txt', 5))
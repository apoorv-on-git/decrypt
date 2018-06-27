#Importing Modules
import hashlib
from itertools import permutations

#Function defined to find the hash
def findHash(originalHash):

	"""
	Decrypting the md5 Hash by forming new words
	and matching their md5 Hash with the Hash
	that is provided

	:param originalHash: Original Hash to be Decrypted
	:return: Decrypted Message or None
	"""

	wordlist = raw_input("What is your wordlist? (Enter the file name) -> ")
	
	#opening the Dictionary Entered
	try:

		wordlistfile = open(wordlist,"r")

	except IOError:
		
		print "Invalid file."

	#Converting the Dictionary into a list
	wordlistfile = list(wordlistfile)
	finallist = []

	#Calculating the number of words in hash
	anagram = raw_input('Enter the anagram -> ')
	words = anagram.count(' ')
	words += 1

	#Saving the list of Unique Characted in the Anagram into a variable charList
	charList = list(set(anagram))
	if ' ' in charList:
		charList.remove(' ')

	index = 0

	#Filtering out the words with letters that are not present in the Anagram
	while index < len(wordlistfile):

		flag = False

		line = wordlistfile[index]

		templine = line.replace('\n', '')

		variable = list(set(templine))
 	
		for i in variable:

			if i not in charList:

				flag = True
				break

		#Forming a new list of filtered words
		if flag == False:

			finallist.append(templine)

		index += 1


	attempt = 1

	#Making the permutations of the Number of words from the filtered list
	for elem in permutations(finallist, 3):

		hashElem = ' '.join(elem)

		#Removing the edge case (Length of the permutation not equal to the length of the Anagram)
		if len(hashElem) != len(anagram):

			continue

		print attempt

		#Converting the permutation into md5 Hash
		m = hashlib.md5()
		m.update(hashElem)
		word_hash = m.hexdigest()

		#Matching the hash generated with the given hash
		if word_hash == originalHash:

			return hashElem

		attempt += 1

if __name__ == "__main__":

	hash = '87bb2bda651995d346c05b5049b4d78b'
	answer = findHash(hash)
	print "Collision!  The word corresponding to the given hash is ", answer
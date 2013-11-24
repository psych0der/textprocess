'''

Module to implement stemming and lemmatization operation on words based on porters algorithm.

'''

vowels = ['a','e','i','o','u']

def isConsonant(word,index):
	if index!=len(word)-1: 
		return word[index] not in vowels and not(word[index]=='y' and isConsonant(word,index+1))

	else:
		return word[index] not in vowels



def measure(word):
	'returns measure of the word'
	mode = 0     # mode 0 : initial(optional consonant); mode 1 : consonant ; mode 2 : vowel
	m = 0
	for index in range(len(word)):
		if isConsonant(word,index):
			if mode == 2:
				m+=1
				mode = 1
		else :
			if mode !=2 :
				mode = 2
	return m

#print measure("aecouciklo")

def containsVowel(word):
	for index in range(len(word)-1):
		if not isConsonant(word,index):
			return True
		
	return False

def endsWithDoubleConsonant(word):
	length = len(word)
	if isConsonant(word,length-1) and isConsonant(word,length-2):
		return True
	else:
		return False

def cvc(word):
	length = len(word)
	if isConsonant(word,length-3):
		if not isConsonant(word,length-2):
			if isConsonant(word,length-1) and (word[length-1] not in ['w','x','y']):
				return True
			else : 
				return False
		else :
			return False
	else :
		return False





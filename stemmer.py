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


def rreplace(s, old, new):
	li = s.rsplit(old, 1)
	return new.join(li)


flag1b = 0


def step1a(word):
	if word.endswith("sses"):
		word = rreplace(word,"sses","ss")
		return word

	if word.endswith("ies"):
		word = rreplace(word,"ies","i")
		return word

	if word.endswith("ss"):
		return word

	if word.endswith("s"):
		word = rreplace(word,"s","")
		return word

	return False


def step1b(word):
	if word.endswith("eed"):
		if measure(rreplace(word,"eed","")) > 0:
			word = rreplace(word,"eed","ee")
			return word

	if word.endswith("ed"):
		if containsVowel(rreplace(word,"eed","")):
			word = rreplace(word,"ed","")
			flag1b = 1
			return word

	if word.endswith("ing"):
		if containsVowel(rreplace(word,"ing","")):
			word = rreplace(word,"ing","")
			flag1b = 1
			return word

	return False

def postStep1b(word):
	if word.endswith("at"):
		word = word+'e'
		return word

	if word.endswith("bz"):
		word = word+'e'
		return word

	if word.endswith("iz"):
		word = word+'e'
		return word

	if endsWithDoubleConsonant(word) and not (word.endswith('l') or word.endswith('s') or word.endswith('z')) :
		word = word[:-1]
		return word

	if measure(word) ==1 and cvc(word) :
		word = word + 'e'

	return False




#w = "motoring"
#print step1b(w)






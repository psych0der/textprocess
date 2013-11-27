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
		return word

	return False

def step2(word):

	if measure(word) > 0:
		if word.endswith("ational"):
			word = rreplace(word,"atinal","ate")
			return word

		if word.endswith("tional"):
			word = rreplace(word,"tional","tion")
			return word

		if word.endswith("enci"):
			word = rreplace(word,"enci","ence")
			return word

		if word.endswith("anci"):
			word = rreplace(word,"anci","ance")
			return word

		if word.endswith("izer"):
			word = rreplace(word,"izer","ize")
			return word

		if word.endswith("abli"):
			word = rreplace(word,"abli","able")
			return word

		if word.endswith("alli"):
			word = rreplace(word,"alli","al")
			return word

		if word.endswith("entli"):
			word = rreplace(word,"entli","ent")
			return word

		if word.endswith("eli"):
			word = rreplace(word,"eli","e")
			return word

		if word.endswith("ousli"):
			word = rreplace(word,"ousli","ous")
			return word

		if word.endswith("ization"):
			word = rreplace(word,"ization","ize")
			return word

		if word.endswith("ation"):
			word = rreplace(word,"ation","ate")
			return word

		if word.endswith("ator"):
			word = rreplace(word,"ator","ate")
			return word

		if word.endswith("alism"):
			word = rreplace(word,"alism","al")
			return word

		if word.endswith("iveness"):
			word = rreplace(word,"iveness","ive")
			return word

		if word.endswith("fulness"):
			word = rreplace(word,"fulness","ful")
			return word

		if word.endswith("ousness"):
			word = rreplace(word,"ousness","ous")
			return word

		if word.endswith("aliti"):
			word = rreplace(word,"aliti","al")
			return word

		if word.endswith("iviti"):
			word = rreplace(word,"iviti","ive")
			return word

		if word.endswith("bility"):
			word = rreplace(word,"bility","ble")
			return word

	else :
		return False


def step3(word):

	if measure(word) > 0:
		if word.endswith("icate"):
			word = rreplace(word,"icate","ic")
			return word

		if word.endswith("ative"):
			word = rreplace(word,"ative","")
			return word

		if word.endswith("alize"):
			word = rreplace(word,"alize","al")
			return word

		if word.endswith("iciti"):
			word = rreplace(word,"iciti","ic")
			return word

		if word.endswith("ical"):
			word = rreplace(word,"ical","ic")
			return word

		if word.endswith("ful"):
			word = rreplace(word,"ful","")
			return word

		if word.endswith("ness"):
			word = rreplace(word,"ness","")
			return word

	else :
		return False


def step4(word):

	if measure(word) > 1:
		if word.endswith("al"):
			word = rreplace(word,"al","")
			return word

		if word.endswith("ence"):
			word = rreplace(word,"ence","")
			return word

		if word.endswith("er"):
			word = rreplace(word,"er","")
			return word

		if word.endswith("ic"):
			word = rreplace(word,"ic","")
			return word

		if word.endswith("able"):
			word = rreplace(word,"able","")
			return word

		if word.endswith("ible"):
			word = rreplace(word,"ible","")
			return word

		if word.endswith("ant"):
			word = rreplace(word,"ant","")
			return word

		if word.endswith("ement"):
			word = rreplace(word,"ement","")
			return word

		if word.endswith("ment"):
			word = rreplace(word,"ment","")
			return word

		if word.endswith("ent"):
			word = rreplace(word,"ent","")
			return word

		if (word[:-3].endswith("t") or word[:-3].endswith("s")) and word.endswith("ion"):
			word = rreplace(word,"ion","")
			return word

		if word.endswith("ou"):
			word = rreplace(word,"ou","")
			return word		

		if word.endswith("ism"):
			word = rreplace(word,"ism","")
			return word

		if word.endswith("ate"):
			word = rreplace(word,"ate","")
			return word

		if word.endswith("iti"):
			word = rreplace(word,"iti","")
			return word

		if word.endswith("ous"):
			word = rreplace(word,"ous","")
			return word

		if word.endswith("ive"):
			word = rreplace(word,"ive","")
			return word

		if word.endswith("ize"):
			word = rreplace(word,"ize","")
			return word					

	else :
		return False


def step5a(word):

	if measure(word[:-1])>1 and word.endswith("e"):
		word = word[:-1]
		return word

	if measure(word[:-1])==1 and not cvc(word[:-1]) and word.endswith("e"):
		word= word[:-1]
		return word

	return False


def step5b(word):
	
	if measure(word)>1 and endsWithDoubleConsonant(word) and word.endswith("l"):
		word = word[:-1]
		return word

	return False





#w = "motoring"
#print step1b(w)






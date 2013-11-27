import re
import tokenizer

'''
Perform basic text normalization which includes
converting all words to lower case except abbreviations 

'''

def normalize(input, multiList=False):
	# input can be string as well as list

	if isinstance(input,str):
		
		line = tokenizer.tokenize(input)
		
		for index,word in enumerate(line):
			# if word is abbreviation or some other important word
			if not re.match(r'^[^a-z]*$',word):
				word.lower()
				line[index] = word.lower() 

		return line

	if not isinstance(input, basestring):
		if multiList==False :
			for index,word in enumerate(input):
			# if word is abbreviation or some other important word
				if not re.match(r'^[^a-z]*$',word):
					input[index] = word.lower()

			return input

		else :
			for list in input:
				for index,word in enumerate(list):
				# if word is abbreviation or some other important word
					if not re.match(r'^[^a-z]*$',word):
						list[index] = word.lower()


			return input



#print normalize('Hello ThEre AKA Hahahah JJk')
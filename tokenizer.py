'''

Tokenizer splits (tokenizes) strings as data pre-processing step.
It excepts file as well as string as an input. 

'''

def tokenize(input, readFile=False):
	# input can be file as well as string
	
	if isinstance(input,file):
		lines = []  	#  list to store lines in the file
		lines = input.readlines()
		lines = [line.replace('\n','').replace('. ',',').replace(':',',').replace('-',',').replace(' ',',').replace(';',',').replace('/',',').replace('\\',',').split(',') for line in lines]
		lines = filter(None, lines)
		return lines

		
	if isinstance(input,str):
		if readFile == True:
			lines = []  	#  list to store lines in the file
			inputFile = open(input)
			lines = inputFile.readlines()
			lines = [line.replace('\n','').replace('. ',',').replace(':',',').replace('-',',').replace(' ',',').replace(';',',').replace('/',',').replace('\\',',').split(',') for line in lines]
			inputFile.close()
			lines = filter(None, lines)
			return lines

		else :
			line = input
			line = line.replace('\n','').replace('. ',',').replace(':',',').replace('-',',').replace(' ',',').replace(';',',').replace('/',',').replace('\\',',').split(',')
			line = filter(None, line)
			return line

#print tokenize('file.txt',readFile=True)


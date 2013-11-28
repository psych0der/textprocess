import tokenizer
import normalizer

'''
Stop word remover removes stop words from a list of words or stringand return strings
It can support multple languges.
Also removes numerical strings.
'''

stopwords = {}	# dictionary to strore stopwords of languages

stopwords['english'] = ['a','able','about','across','after','all','almost','also'
,'am','among','an','and','any','are','as','at','be','because','been','but','by',
'can','cannot','could','dear','did','do','does','either','else','ever','every',
'for','from','get','got','had','has','have','he','her','hers','him','his','how',
'however','i','I','if','in','into','is','it','its','just','least','let','like','likely',
'may','me','might','most','must','my','neither','no','nor','not','of','off','often',
'on','only','or','other','our','own','rather','said','say','says','she','should',
'since','so','some','than','that','the','their','them','then','there','these',
'they','this','tis','to','too','twas','us','wants','was','we','were','what',
'when','where','which','while','who','whom','why','will','with','would','yet','you','your']




def remove_stop_word(input,multiList=False):
	if isinstance(input,str):
		filtered = [word for word in normalizer.normalize(input) if (word not in stopwords['english'] and not word.isdigit())]
		return filtered

	if not isinstance(input, basestring):
		if multiList == True:
			for index,lst in input:
				input[index] = [word for word in normalizer.normalize(lst) (word not in stopwords['english'] and not word.isdigit())]
			return input

		else :
			input = [word for word in normalizer.normalize(input) (word not in stopwords['english'] and not word.isdigit())]
			return input


#print tokenizer.tokenize('sdfdsf sdffsd sdfsdfds')
#print remove_stop_word('hello i Am mayank. I Am a Good boy')
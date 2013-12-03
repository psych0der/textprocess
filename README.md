textprocess
==========

a python module for text preprocessing.

Overview
----------

text process performs 5 stage filtering viz. tokenisation, normalisation, stop word removal, stemming and lemmatisation which can be used as preprocessing step required in NLP,machine learning and other linguistic programming domains. Relevant for datasets used in data mining.

Features
----------
* Supports global filtering which performs all 5 filtering as well as separate filtering.
* Accepts list as well as string as  input.

Installation
----------

```shell
pip install textprocess

```
Usage
----------

#### Tokenization

```python
from textprocess import tokenizer
input = 'this is a test string'
tokenized = tokenizer.tokenize(input)
tokenized
['this', 'is', 'a', 'test', 'string']
```

tokenize accepts string as well as file object to read from.For reading file pass readFile = true

```python
from textprocess import tokenizer
input = open('input.txt')
tokenized = tokenizer.tokenize(input, readFile=True)
```    

* Following functions accepts string , list , multilist(pass multilist=True)
* Tokenization is implicitely called in following functions

____

#### Normalization

```python
from textprocess import normalizer
input = 'ThIs Is DiRTy TeXT'
normalized = normalizer.normalize(input)
normalized
['this', 'is', 'dirty', 'text']
```

#### Stop Word removal

```python
from textprocess import stopwordremover
input = 'Hello i am Mayank Bhola. Do what you like, like what you do'
filtered = stopwordremover.remove_stop_word(input)
filtered
['hello', 'mayank', 'bhola']
```
  

#### Stemming/Lemmatization
Performs stemming as well as lemmatization

* Tokenization and normalization are implicotely called
* Pass cascade=False for skipping stop word removal

```python
from textprocess import stemmer
input = 'Text containing lot of examples and forms is considered to be legitimate'
filtered = stemmer.lemmatize(input,cascade=False)
filtered
['text', 'contain', 'lot', 'of', 'examp', 'and', 'form', 'i', 'consid', 'to', 'be', 'legitim']
```


Licence
----------
MIT

Live Demo
----------
You can test the public on cloud by visiting this URL
(textprocess)[http://cloudpreprocessing.herokuapp.com]

Flask app credits : (Shivam Bansal)[https://github.com/shivam5992]


  
    

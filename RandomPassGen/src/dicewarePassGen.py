#! /usr/bin/python

import urllib2, sys, string, operator

wordList = []
numList = []
numWords = 0
passWd = []


###    Open a connection to random.org
conn = urllib2.urlopen('http://www.random.org/integers/?num=45&min=1&max=6&col=5&base=10&format=plain&rnd=new')
html = conn.read()
ranNums = html.split('\n')
i=0
for each in ranNums:
    ranNums[i] = each.replace("\t","")
    i += 1
ranNums = filter(None, ranNums)

###    Load diceware word list
dicewords = open("beale.wordlist")
fileWordsAndNums = dicewords.readlines();

###    Separate words and corresponding diceware number combinations in parallel lists
for line in fileWordsAndNums:
    wordAndNum = string.split(line,maxsplit=1)
    wordList.append(wordAndNum[1])
    numList.append(wordAndNum[0])
    numWords += 1

for ranNum in ranNums:
    ind = 0
    
    while ranNum != numList[ind]:
        ind += 1
        
    passWd.append(wordList[ind])
    

    

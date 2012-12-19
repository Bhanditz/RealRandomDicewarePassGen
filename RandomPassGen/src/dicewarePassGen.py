#! /usr/bin/python

import urllib2, sys, string

wordList = []
numList = []
numWords = 0

conn = urllib2.urlopen('http://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new')
html = conn.read()
dicewords = open("src/beale.wordlist")
fileWordsAndNums = dicewords.readlines();

for line in fileWordsAndNums:
    wordAndNum = string.split(line, '\t')
    wordList.append(wordAndNum[1])
    numList.append(wordAndNum[0])
    numWords += 1
    
    
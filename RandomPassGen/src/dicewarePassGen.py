#! /usr/bin/python

import urllib2, sys, string, operator

wordList = []
numList = []
numWords = 0
passWd = []

#Prompt the user for the number of Diceware words
print '\
*****************************************************************************\n\
EVERYONE READ!:\n\
THe password generated by this method is completely secure PROVIDED the\n\
numbers are not intercepted before they reach your computer. Due to\n\
limitations in the API from Random.org the request is done through\n\
insecure HTTP request. Also if your computer is under surveillance\n\
or a spy is behind you it is also useless.  The most secure method\n\
remains as always, a real dice and paper. Know the risks.\n\
\n\
FOR THE TECHNICALLY INCLINED:\n\
Each word in your Diceware passphrase \n\
yields 12.9 bits of entropy, the way passphrase security is measured. A five \n\
word Diceware passphrase would have an entropy of at least 64.6 bits; six \n\
words would have 77.5 bits, seven words 90.4 bits. Inserting a letter at \n\
random adds about 10 bits of entropy. Try and find the right balance\n\
between password strength and memorability.\n\
*****************************************************************************\n'
numWordsNeeded = int(raw_input("Enter the number of diceware words required: ").strip())


### TODO:  Add random characters from table of ASCII
### specialCharsFlag = raw_input("Do you want any special characters?(yn)     ").strip()
### if specialCharsFlag == 'y':
###        numSpecial  = int(raw_input("How many?                                   ").strip())
### numWordsNeeded = numWordsNeeded * 5
#print numWordsNeeded
###    Open a connection to random.org

conn = urllib2.urlopen('http://www.random.org/integers/?num='+str(5*numWordsNeeded)+'&min=1&max=6&col=5&base=10&format=plain&rnd=new')
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

###    Open generated file for writing
passFile =  open("DicewarePass.txt", 'w')

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
    passFile.write(wordList[ind].replace('\n',' '))
dicewords.close()
passFile.close()

    

    

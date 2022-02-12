#usethisforyourmainstuff
import time
from collections import Counter
start=time.time()
BLANK=0
YELLOW=1
GREEN=2
ambiguityCounter=Counter()
ambigWordSet=set()
def wordleResponse(guess,real):
    response=[BLANK]*5
    reallist=list(real.upper())
    guess=guess.upper()
    for i in range(0,5):
        if(guess[i]==reallist[i]):
            reallist[i]=""
            response[i]=GREEN
    #print(reallist)
    for i in range(0,5):
        if(guess[i] in reallist and response[i]==BLANK):
            reallist.remove(guess[i])
            response[i]=YELLOW
    return response
wordset=[]
for i in range(0,4):
    wordset.append(input("word: ").strip())

with open("wordle-answers-alphabetical.txt") as file:
    allwords=[i.strip() for i in file.readlines()]
testwords=allwords

for testWord in testwords:
    responses=[]
    for answerWord in wordset:
        responses.append(wordleResponse(answerWord,testWord))
    for possibleword in allwords:
        tempResponses=[]
        for answerWord in wordset:
            tempResponses.append(wordleResponse(answerWord,possibleword))
        if(tempResponses==responses and testWord!=possibleword):
            #print(testWord+" has ambiguity w "+possibleword)
            ambiguityCounter[testWord]+=1
            if(ambiguityCounter[testWord]==2):
                ambigWordSet.add(testWord)
           
        
end=time.time()
print(end-start)
print(ambigWordSet)
print(len(ambigWordSet))

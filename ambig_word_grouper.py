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
wordset=["tubes","fling","champ","wordy"]
with open("wordle-answers-alphabetical.txt") as file:
    allwords=[i.strip() for i in file.readlines()]

#testwords=allwords
testwords=['savvy', 'steer', 'ester', 'reset',
           'viper', 'sassy', 'vague', 'gauze',
           'piper', 'gauge', 'riper', 'stake',
           'state', 'stave', 'assay', 'skate']
wordgroupdicts=dict()
for testWord in testwords:
    responses=[]
    for answerWord in wordset:
        responses.append(wordleResponse(answerWord,testWord))
    for possibleword in testwords:
        tempResponses=[]
        for answerWord in wordset:
            tempResponses.append(wordleResponse(answerWord,possibleword))
        if(tempResponses==responses and testWord!=possibleword):
            print(testWord+" has ambiguity w "+possibleword)
            if(str(tempResponses) in wordgroupdicts.keys()):
                wordgroupdicts[str(tempResponses)].add(testWord)
                wordgroupdicts[str(tempResponses)].add(possibleword)
            else:
                wordgroupdicts[str(tempResponses)]=set()
                wordgroupdicts[str(tempResponses)].add(testWord)
                wordgroupdicts[str(tempResponses)].add(possibleword)
end=time.time()
print(end-start)

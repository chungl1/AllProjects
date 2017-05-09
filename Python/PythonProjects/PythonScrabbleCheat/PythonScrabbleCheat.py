import enchant
import itertools

def main():
    highValue = 0
    wordList = []
    bestWord = ""
    ascii = 97
    stringOne = raw_input("Please type in the letters on your scrabble rack. Leave an empty space if you have a blank: ")
    stringOne = stringOne.lower()
    stringTwo = list(stringOne)

    if " " in stringTwo: 
        stringTwo.remove(" ")
        while (ascii <= 122): 
            b = chr(ascii)
            stringTwo.insert(0, b)
            for i in range(1,len(stringTwo)+1):
                stringOne = ''.join(stringTwo)
                words = list(wordGenerator(stringOne, i))
                wordList.append(words)
                for j in range(0,len(wordList[0])):
                    wordValidity = wordVerification(wordList[0][j])
                    if wordValidity==True:
                        tileValue = readTileValues(wordList[0][j])
                        if tileValue>highValue:
                            highValue = tileValue
                            bestWord = wordList[0][j]
                wordList = []
            stringTwo.remove(b)
            ascii = ascii + 1
    else:        
        for i in range(1,len(stringTwo)+1):
            words = list(wordGenerator(stringOne, i))
            wordList.append(words)
            for j in range(0,len(wordList[0])):
                wordValidity = wordVerification(wordList[0][j])
                if wordValidity==True:
                    tileValue = readTileValues(wordList[0][j])
                    if tileValue>highValue:
                        highValue = tileValue
                        bestWord = wordList[0][j]
            wordList = []

    if highValue == 0: 
        print "There are no possible words"
    else:
        print "Your best possible combination is the word ",bestWord, " for a score of ",highValue,"!"
       
def wordVerification(currentWord):
    A = enchant.Dict("en_US")
    if A.check(currentWord) == True:
        if len(currentWord) > 1:
            return True
        else:
            return False
    else:
        return False

def readTileValues(word):
    valueOfWord = 0 
    fileOne = open("TileValues.txt", 'r')
    values = fileOne.read()
    for i in range(len(word)):
        index = values.index(word[i])
        if values[index+1].isdigit()==True:
            if values[index+2].isdigit()==True:
                valueOfTile = int(values[index+1]+values[index+2])
            elif values[index+2].isdigit()==False:
                valueOfTile = int(values[index+1])
        valueOfWord = valueOfWord + valueOfTile

    fileOne.close()

    return valueOfWord

def wordGenerator(stringOne, i):
    words = [''.join(p) for p in itertools.permutations(stringOne, i)]
    return words

main()





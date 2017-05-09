import enchant
import itertools

def main():
    highValue = 0
    wordList = []
    bestWord = ""
    ascii = 97
    print "This program gives the best possible letter combination for your game of Scrabble, assuming that acronyms are not words. Beat your friends!"
    stringOne = raw_input("Please type in the letters on your scrabble rack. Leave an empty space if you have a blank: ")
    stringOne = stringOne.lower()
    stringTwo = list(stringOne)
    tempList = []

    if " " in stringTwo: 
        stringTwo.remove(" ")
        while (ascii <= 122): #First removes empty space, replaces with letter. At next iteration, removes that letter, replaces with next in alphabet#
            b = chr(ascii)
            stringTwo.insert(0, b)
            if allConsonants(stringTwo) == True:
                for i in range(1,len(stringTwo)+1):
                    stringOne = ''.join(stringTwo)
                    words = list(wordGenerator(stringOne, i))
                    wordList.append(words)
                    for j in range(0,len(wordList[0])): #Test word validity and compares scores#
                        wordValidity = wordVerification(wordList[0][j])
                        if wordValidity==True:
                            tileValue = readTileValues(wordList[0][j])
                            if tileValue>highValue:
                                highValue = tileValue
                                bestWord = wordList[0][j]
                    wordList = []
            stringTwo.remove(b)
            ascii = ascii + 1
        if highValue == 0: 
            print "There are no possible words"
        else:
            print "Your best possible combination is the word ",bestWord, " for a score of ",highValue,"!"
    else:
        if allConsonants(stringTwo) == True:
            for i in range(1,len(stringTwo)+1): #Runs through cases without blanks#
                words = list(wordGenerator(stringOne, i))
                tempList.append(words)
                wordList = wordListFunction(tempList) #Eliminates words with only consonants#
                for j in range(0,len(wordList)):
                    wordValidity = wordVerification(wordList[j])
                    if wordValidity==True:
                        tileValue = readTileValues(wordList[j])
                        if tileValue>highValue:
                            highValue = tileValue
                            bestWord = wordList[j]
                wordList = []
                tempList = []
        if highValue == 0: 
            print "There are no possible words"
        else:
            print "Your best possible combination is the word ",bestWord, " for a score of ",highValue,"!"

    
       
def wordVerification(currentWord): #Uses pyEnchant library to check validity of words, returns true or false#
    A = enchant.Dict("en_US")
    if A.check(currentWord) == True:
        if len(currentWord) > 1:
            return True
        else:
            return False
    else:
        return False

def readTileValues(word): #Uses textfile to detect scores for letters and returns the score of the word#
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

def wordGenerator(stringOne, i): #Returns a generated letter combination using iterTools library#
    words = [''.join(p) for p in itertools.permutations(stringOne, i)]
    return words

def allConsonants(stringTwo):
    if chr(97) not in stringTwo:
        if chr(101) not in stringTwo:
            if chr(105) not in stringTwo:
                if chr(111) not in stringTwo:
                    if chr(117) not in stringTwo:
                        if chr(121) not in stringTwo:
                            return False
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return True
    else:
        return True

def wordListFunction(tempList):
    tempWordList = []
    for i in range(0, len(tempList[0])):
        if allConsonants(tempList[0][i])==True:
            tempWordList.append(tempList[0][i])
    return tempWordList
                        

main()





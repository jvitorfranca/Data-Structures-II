import word as wd
import unidecode as un
import re
import red_black_tree as rbt
import hash_table as ht


C = 4
dTerms = {}

def comp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    return 0
    
def compWords(x, y):
    global C
    if x[0:C] > y[0:C]:
        return 1
    elif x[0:C] < y[0:C]:
        return -1
    return 0

def loadRedBlackTree(words):
    tree = rbt.RedBlackTree()

    for key, word in words.items():
        tree.insert(word, compWords)

    return tree

def loadHashTable(words):
    hashSize = int(input("Insert the size of the hash: "))

    hesh = ht.HashTable(hashSize)

    for key, word in words.items():
        hesh.insert(word, key)

    return hesh

def loadWords(files):
    global C
    global dTerms
    C = int(input("Digite o valor do parâmetro C: "))

    print(files)

    words = {}
    i = 1
    for fil in files:
        f = open(fil, "r")
        dTerms[fil] = 0
        fileWords = {}
        for line in f:
            for word in re.split('; |, |\*|\n|;|!|\?|\.|\t| ', line):
                if len(word) < C:
                    continue
                theWord = un.unidecode(word.lower())
                if theWord not in words:
                    words[theWord] = wd.Word(theWord, len(files))
                if theWord not in fileWords:
                    fileWords[theWord] = theWord
                    dTerms[fil] += 1
                words[theWord].incrementOccurs(i)
        i = i + 1
        f.close()
    
    return words
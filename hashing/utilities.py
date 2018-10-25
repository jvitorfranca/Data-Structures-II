import word as wd
import unidecode as un
import re
import math
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

def loadHashTable(words, option):
    hashSize = int(input("Insert the size of the hash: "))

    hesh = ht.HashTable(hashSize)

    if option == 'linear':
        for key, word in words.items():
            hesh.insert(word, key, 'linear')
    elif option == 'quadratic':
        for key, word in words.items():
            hesh.insert(word, key, 'quadratic')

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

def IDF(files, tad, tadStr):
    global dTerms
    N = len(files)
    L = 0.05
    
    strtermos = str(input("Insira os termos da consulta: "))
    termos = strtermos.split()

    i = 0
    weights = []
    for termo in termos:
        if tadStr == "hash":
            word = tad[termo]
        else:
            word = tad.search(termo, compWords)
        fN = 1
        weights.append([])
        if word is None:
            for fil in files:
                weights[i].append(0)
            i += 1
            continue
        dj = 0
        dj = word.getQFilesWOccurs(termo)
        for fil in files:
            f = word.getOccursFile(fN)
            weights[i].append(f * (math.log(N, 2)/dj))
            fN += 1
        i += 1

    IDF = []
    fN = 1
    for fil in files:
        tSum = 0
        i = 0
        for item in termos:
            tSum += weights[i][fN-1]
            i += 1
        IDF.append((1/dTerms[fil]) * tSum)
        fN += 1

    IDFcpy = list(IDF)
    IDF.sort(reverse=True)
    
    for idf_term in IDF:
        if idf_term < L:
            continue
        i = IDFcpy.index(idf_term)
        print(files[i], idf_term)
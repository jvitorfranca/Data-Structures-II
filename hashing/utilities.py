import word as wd
import unidecode as un
import re
import math
import red_black_tree as rbt
import hash_table as ht


C = 4
dTerms = {}

# Function to compare two integers
def comp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    return 0
    
# Function to compare two words, given the parameter C
def compWords(x, y):
    global C
    if x[0:C] > y[0:C]:
        return 1
    elif x[0:C] < y[0:C]:
        return -1
    return 0

# Calling RedBlack class given the inputs
def loadRedBlackTree(words):
    tree = rbt.RedBlackTree()

    # Inserting the words in the ADT
    for key, word in words.items():
        tree.insert(word, compWords)

    return tree

# Calling HashTable class given the inputs
def loadHashTable(words, option):
    hashSize = int(input("Insert the size of the hash: "))

    hesh = ht.HashTable(hashSize)

    # Inserting differentely depending on the parameter
    if option == 'linear':
        for key, word in words.items():
            hesh.insert(word, key, 'linear')
    elif option == 'quadratic':
        for key, word in words.items():
            hesh.insert(word, key, 'quadratic')

    return hesh

# Putting the inputs into a instance 'word'
def loadWords(files):
    global C
    global dTerms
    C = int(input("Insert the value of C: "))

    print(files)

    words = {}
    i = 1
    for fil in files:

        # Reading the files
        f = open(fil, "r")
        dTerms[fil] = 0
        fileWords = {}
        for line in f:
            # Eliminating non valid characters
            for word in re.split('; |, |\*|\n|;|!|\?|\.|\t| ', line):
                # Checking if the word's smaller than the parameter C
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

# Function to calculate the Inverse Document Frequency
def IDF(files, tad, tadStr):
    global dTerms
    N = len(files)
    L = 0.05
    
    # Words wanted to search
    strtermos = str(input("Insert the words you want to search: "))
    termos = strtermos.split()

    i = 0
    weights = []
    for termo in termos:
        # Checking which ADT were choosen and searching
        if tadStr == "hash":
            word = tad[termo]
        else:
            word = tad.search(termo, compWords)
        # Calculating the weight
        fN = 1
        weights.append([])
        if word is None:
            for fil in files:
                weights[i].append(0)
            i += 1
            continue
        dj = 0
        dj = word.getQFilesWOccurs(termo)
        # Calculating the relevance
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
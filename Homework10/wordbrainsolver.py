"""the python code for wordbrainsolver game"""

# Copyright 2017 Simin Zhai siminz@bu.edu
# Copyright 2017 Zulin Liu liuzulin@bu.edu
# Copyright 2017 Jafallac James jafallac@bu.edu
# Copyright 2017 Yu Zhao yuzhao95@bu.edu
from sys import argv


SIMPLELETTERSET = open(argv[1], 'rt').read().split()
DIFFICULTWORDSET = open(argv[2], 'rt').read().split()
SIMPLELETTERSET1 = {}
DIFFICULTWORDSET1 = {}
SIMPLELETTERCHECK = {}
DIFFICULTWORDCHECK = {}
LETTERSET = []
LENGTHSET = []
LINE = ""

for word in SIMPLELETTERSET:
    SIMPLELETTERSET1.setdefault(len(word), set())
    SIMPLELETTERSET1[len(word)].add(word)
    for j, __ in enumerate(word):
        SIMPLELETTERCHECK.setdefault(j, set())
        SIMPLELETTERCHECK[j].add(word[:j])

for word in DIFFICULTWORDSET:
    DIFFICULTWORDSET1.setdefault(len(word), set())
    DIFFICULTWORDSET1[len(word)].add(word)
    for k, __ in enumerate(word):
        DIFFICULTWORDCHECK.setdefault(k, set())
        DIFFICULTWORDCHECK[k].add(word[:k])


def wordmatching(wordmatch, shape):
    """word matching"""
    if shape == '*' * len(shape):
        return True
    else:
        for i, char in enumerate(wordmatch):
            if shape[i] != '*' and char != shape[i]:
                return False
    return True


def wordconvert(charlist):
    """return the position of word as a list"""
    matchdictionary = {}
    for __i__, line in enumerate(charlist):
        for __j__, char in enumerate(line):
            matchdictionary[(__i__, __j__)] = char
    return matchdictionary


def listreduce(matrix, place):
    """reduce the list when we diminish the letter"""
    newlist = dict(matrix)
    if place == []:
        return newlist
    for pos in place:
        del newlist[pos]
    while True:
        reduced = True
        newlist_copy = dict(newlist)
        for letter in newlist:
            if letter[0] + 1 in range(VEIDOO) and \
               (letter[0] + 1, letter[1]) not in newlist.keys():
                reduced = False
                newlist_copy[(letter[0] + 1, letter[1])] \
                    = newlist_copy[(letter)]
                del newlist_copy[letter]
        if reduced:
            return newlist_copy
        else:
            newlist = newlist_copy


class WordList:
    """the characters of list"""

    def __init__(self):
        self.matrix = wordconvert(LETTERSET)
        self.wordfoundlist = []
        self.result = [("", self.matrix)]
        self.dict = {}
        self.check = {}
        self.situation = 'easy'
        self.suchlen = 0

    def wordsearch(self, matrix, initial, partofletter, letterplace):
        """search for a the start of letter"""
        xpostion, ypostion = initial
        partofletter = partofletter + matrix[(xpostion, ypostion)]
        localposlist = list(letterplace)
        localposlist.append((xpostion, ypostion))
        if partofletter not in self.check[len(partofletter)]:
            return 0
        for cell in [(xpostion - 1, ypostion - 1), (xpostion - 1, ypostion),
                     (xpostion, ypostion - 1), (xpostion + 1, ypostion - 1),
                     (xpostion - 1, ypostion + 1), (xpostion + 1, ypostion),
                     (xpostion, ypostion + 1), (xpostion + 1, ypostion + 1)]:
            if cell not in letterplace \
                    and cell in matrix.keys():
                if len(partofletter) + 1 == self.suchlen:
                    newword = partofletter + matrix[cell]
                    if newword in self.dict:
                        self.wordfoundlist.append([newword] +
                                                  localposlist +
                                                  [cell])
                    else:
                        pass
                else:
                    self.wordsearch(matrix, cell, partofletter, localposlist)

    def findwords(self):
        """puzzle solutions """
        for i, length in enumerate(LENGTHSET):
            self.suchlen = length
            if self.situation == 'easy':
                SIMPLELETTERSET1.setdefault(length, set())
                self.dict = SIMPLELETTERSET1[length]
                self.check = SIMPLELETTERCHECK
            else:
                DIFFICULTWORDSET1.setdefault(length, set())
                self.dict = DIFFICULTWORDSET1[length]
                self.check = DIFFICULTWORDCHECK
            formerresult = list(self.result)
            self.result = []
            for content in formerresult:
                formerword, newlist = content
                self.wordfoundlist = []
                for initial in newlist:
                    self.wordsearch(newlist, initial, "", [])
                for content in self.wordfoundlist:
                    newword = content[0]
                    newpositions = content[1:]
                    if not wordmatching(newword, PATTERNLIST[i]):
                        continue
                    self.result.append((formerword + ' ' + newword,
                                        listreduce(newlist, newpositions)))
            if self.result == []:
                if self.situation == 'easy':
                    self.situation = 'hard'
                    self.result = [("", self.matrix)]
                    self.findwords()
                    break
                else:
                    break


while True:
    try:
        LINE = input()
    except EOFError:
        exit(0)
    if LINE == '':
        break
    if '*' in LINE:
        LENGTHSET = []
        PATTERNLIST = []
        VEIDOO = len(LETTERSET)
        for __ in LINE.split():
            LENGTHSET.append(len(__))
            PATTERNLIST.append(__)
        MW = WordList()
        MW.findwords()
        OUTPUT = sorted(set([__[0] for __ in MW.result]))
        for l in OUTPUT:
            print(l)
        print('.')
        LETTERSET = []
        LENGTHSET = []
    else:
        LETTERSET.append(list(LINE))

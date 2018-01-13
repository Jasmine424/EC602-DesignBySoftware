# Copyright 2017 Simin Zhai siminz@bu.edu
# Copyright 2017 Zulin Liu liuzulin@bu.edu
# Copyright 2017 James Fallacara jafallac@bu.edu

'''python wordplayer program'''

import itertools
import sys


def possibility(letter, length, num):
    '''delete charater which is the same'''
    if len(letter) != num:
        return False
    for char in letter:
        if char not in length:
            return False
        buffers = length.replace(char, "", 1)
        if len(buffers) != len(length)-1:
            return False
        else:
            length = buffers
    return True
with open(sys.argv[1], 'r') as k:
    WORDS = list(map(tuple, k.read().split()))
WORDLIST1 = {}
WORDLIST2 = {}
for word in WORDS:
    a = tuple(sorted(word))
    b = len(word)
    if a in WORDLIST2:
        WORDLIST2[a].add(word)
    else:
        WORDLIST2[a] = set()
        WORDLIST2[a].add(word)
    if b in WORDLIST1:
        WORDLIST1[b].add(word)
    else:
        WORDLIST1[b] = set()
        WORDLIST1[b].add(word)
while True:
    CHARACTERS, NUMBER = input().split()
    NUMBER = int(NUMBER)
    if NUMBER == 0:
        break
    L = tuple(sorted(CHARACTERS))
    if len(CHARACTERS)-NUMBER > 5:
        if NUMBER in WORDLIST1:
            WORDLIST = sorted([''.join(word)
                               for word in WORDLIST1[NUMBER]
                               if possibility(word, CHARACTERS, NUMBER)])
            if len(WORDLIST) != 0:
                print(*WORDLIST, sep='\n')
    else:
        WORDLIST = [list(map(''.join, WORDLIST2[combination]))
                    for combination in itertools.combinations(L, NUMBER)
                    if combination in WORDLIST2]
        if len(WORDLIST) != 0:
            print(*sorted(set(itertools.chain.from_iterable(WORDLIST))),
                  sep='\n')
    print('.')

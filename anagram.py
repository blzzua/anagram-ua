#!/bin/python3
# coding=utf-8
import itertools
import sys
import os
# from os import system as shellexec
shellexec = os.system

def init_dict():
    if not os.path.isfile('uadict.txt'):
        shellexec( "aspell -l uk dump master | aspell -l uk expand |  tr ' ' '\n'  > uadict.txt")

def test_word( word ):
    #remove nonalphabet symbol
    word = ''.join([letter for letter in word if letter in alphabet])
    ret_value=bool()
    consmask=''.join( [ str(consonant[i]) for i in word ] )
    # 4 подряд согласные/ 3 подряд гласные
    if ( ( '1111' in consmask ) or ('000' in consmask) ):
        ret_value = False
    else:
        ret_value = True
    return ret_value

if __name__ == '__main__' :
    resfile = open ('/tmp/permutations.txt', mode = 'w', encoding='utf8' )

    if len(sys.argv) > 0:
        word = sys.argv[1]
        word_len = len(word)
    else:
        os._exit(1)
    init_dict()

    same_len_words = list()
    with open('uadict.txt', 'r') as f:
        while True:
            line = f.readline()
            if line:
                if len(line.strip()) == word_len:
                    same_len_words.append(line.strip())
            else:
                break

    ## len, count statistics:
    """
    01    8
    02    117
    03    1389
    04    7182
    05    24217
    06    54478
    07    104090
    08    160706
    09    204320
    10    222147
    11    207763
    12    170281
    13    123577
    14    83003
    15    52937
    16    31515
    17    18789
    18    11142
    19    7123
    20    4443
    21    2864
    22    1910
    23    1221
    """

    for i in itertools.permutations(word):
        if ''.join(i) in same_len_words:
            print(''.join(i))


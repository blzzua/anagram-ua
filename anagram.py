#!/bin/python3
# coding=utf-8
import itertools
import sys
import os
# from os import system as shellexec
shellexec = os.system

alphabet = ( 'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', \
             'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я' )
consonant =  { 'а': 0, 'б': 1, 'в': 1, 'г': 1, 'ґ': 1, 'д': 1, 'е': 0, 'є': 0, 'ж': 1, 'з': 1, 'и': 0, \
               'і': 0, 'ї': 1, 'й': 1, 'к': 1, 'л': 1, 'м': 1, 'н': 1, 'о': 0, 'п': 1, 'р': 1, 'с': 1, \
               'т': 1, 'у': 0, 'ф': 1, 'х': 1, 'ц': 1, 'ч': 1, 'ш': 1, 'щ': 1, 'ь': 1, 'ю': 0, 'я': 0 }

def test_word( word ):
    #remove alphabet symbol
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
    shellexec( "aspell -l uk dump master | aspell -l uk expand |  tr ' ' '\n'  > /tmp/uadict.txt")
    resfile = open ('/tmp/permutations.txt', mode = 'w', encoding='utf8' )
    word = 'пирлакан'
    if len(sys.argv) > 0:
        word = sys.argv[1]
    for i in itertools.permutations( word ):
        if test_word (i):
            resfile.writelines (''.join(i)+'\n')
    resfile.close()
    shellexec("fgrep -w -f /tmp/permutations.txt /tmp/uadict.txt || fgrep -f /tmp/permutations.txt /tmp/uadict.txt  ")


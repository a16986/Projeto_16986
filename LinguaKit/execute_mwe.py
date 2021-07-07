#!/usr/bin/env python3 

import sys
import os   


for nomeFicheiro in sys.argv[1:]:
       
       nomeFicheiro_fin = nomeFicheiro.replace('.txt', '')
       command = './linguakit mwe pt ' + nomeFicheiro + ' -mi  > ' + nomeFicheiro_fin + '_output-mutualinformation.txt'
       os.system(command)

       command = './linguakit mwe pt ' + nomeFicheiro + ' -cooc  > ' + nomeFicheiro_fin + '_output-ngrams.txt'
       os.system(command)


#!/usr/bin/env python3 

import sys   
import re


def remove_accents(a):
    a = re.sub(u"[àáâãäå]", 'a', a)
    a = re.sub(u"[èéêë]", 'e', a)
    a = re.sub(u"[ìíîï]", 'i', a)
    a = re.sub(u"[òóôõö]", 'o', a)
    a = re.sub(u"[ùúûü]", 'u', a)
    a = re.sub(u"[ýÿ]", 'y', a)
    a = re.sub(u"[ß]", 'ss', a)
    a = re.sub(u"[ñ]", 'n', a)
    return a





file = open(sys.argv[1], "r")
words = file.readlines()
file.close()
n = 0

common_words = {}

for word in words:
    common_words[word.replace('\n','')] = n
    n = n + 1



dic = dict()

for nomeFicheiro in sys.argv[3:]:
   
    
    symbols = '%|▼| |&|/|,|-|\.|•|−|≥|→|▼|≤|–|×|:|;|’|‘|º'
    file2 = open(nomeFicheiro , "r", encoding = "utf-8")
    sentences = file2.readlines()
    file2.close()

    for sentence in sentences:
        filtered_sentence = re.split('\t', sentence)
        if filtered_sentence[0] != '\n': #passa todas as frases que contêm apenas uma linha branca
            
            words = re.split(symbols, filtered_sentence[0]) #obtem todas as palavras para a analise
           
            aux = 0 #0 = são todas comuns

            for word in words:
                         
                if aux == 1 or word.isnumeric() == True or len(word) <= 1: 
                    continue
                if remove_accents(word.lower()) not in common_words:
                    aux = 1 #1 = alguma é incomum
            
            
            if aux == 1:
                temp = ''
                for wor in words:

                    if  wor.isnumeric() == False and len(wor) > 1:   
                        temp += wor + ' '
                        
                        
                        
                if temp in dic:
                    dic[temp] += float(filtered_sentence[1])
                else:
                    dic[temp] = float(filtered_sentence[1]) 
               
            
    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    with open(sys.argv[2], 'w') as f:
        for i in sorted_dic:
            f.write(i[0] + '\t' + str(i[1]) +'\n')  
              

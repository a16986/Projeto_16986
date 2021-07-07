#!/usr/bin/env python3
import sys


dic = dict()

#faz o somatorio de de dicionarios
for nomeFicheiro in sys.argv[2:]:

    with open(nomeFicheiro, 'r', encoding = 'utf8') as file:
        sentences = file.readlines()
        file.close()
    
    for sentence in sentences: # nao lê a primeira linha de introdução
        
        words = sentence.split('\t') # obtem a palavra e o numero de vezes utilizada
       
        temp = 0
        words[1] = words[1].replace('\n','') # transforma-a de maneira a que seja adaptavel a inteiro
        if words[0] in dic:
            dic[words[0]] += int(words[1])
        else:
            dic[words[0]] = int(words[1])  
     
    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    
with open(sys.argv[1], 'w') as outfile:
        for i in sorted_dic:
            outfile.write(i[0] + '\t' + str(i[1]) +'\n')  
              

#!/usr/bin/env python3

import re
import sys

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

for nomeFicheiro in sys.argv[2:]:

    file2 = open(nomeFicheiro , "r", )
    sentences = file2.readlines()
    file2.close()
    
    temp = '' #da store as palavra enquanto elas forem seguidas
    aux = 0 #verifica se a palavra sao incomuns e seguidas
    
    uncommon_words = {}
    for sentence in sentences:
    
        words = sentence.split()
        for word in words:
                                    
            clean_words = re.split('[^a-zA-ZÀ-ÿ]', word)

            aux1 = ''
            aux2 = 0
            
            for clean_word in clean_words:
                if clean_word != '':
                    if aux1 == '':
                        aux1 = clean_word
                    else:
                        aux1 = aux1 + '-' + clean_word
                        aux2 = 1
                        
                if aux2 == 1:
                    clean_words.clear()
                    clean_words.append(aux1)

            for clean_word in clean_words:
                
                if remove_accents(clean_word.lower()) not in common_words and len(clean_word) > 1 and clean_word.isnumeric() == False and clean_word != '' :
                    
                    
                    if aux == 0 and temp == '': #faz o primeiro ciclo para quando temp == ''
                        temp = clean_word

                        aux = 1
                        
                    elif aux == 0 and temp != '':
                        #reponsavel por guardar a(s) palavra(s) temp
                        if temp in uncommon_words:
                            uncommon_words[temp] += 1
                        else:
                            uncommon_words[temp] = 1
                        aux = 1
                        temp = clean_word

                        
                    elif aux == 1:
                        #rensponsavel por juntar palavras juntas
                        temp = temp + ' ' + clean_word

                else:
                    #da reset as palavras caso seja comum
                    aux = 0
            #guarda o ultimo temp        
        
        aux = 0 #da reset à leitura de conjuntos quando termina a leitura de uma frase
        
    #recorda o ultimo conjunto de palavras obtido    
    if temp in uncommon_words:
        uncommon_words[temp] += 1
    else:
        uncommon_words[temp] = 1
                                            
    nomeFicheiro = nomeFicheiro.replace('.txt', '')                    
    with open(nomeFicheiro + '_uncommon.txt'  , 'w') as outfile:
        for key, value in uncommon_words.items():
            outfile.write('%s\t%s\n' % (key,value))
        
    sentences.clear()
    uncommon_words.clear()

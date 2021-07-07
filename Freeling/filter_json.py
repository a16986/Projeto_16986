#!/usr/bin/env python3
import sys
import json
import re


def search_words(jsonObject, nomeFicheiro):
    wanted_list = [] #dicionario que contem as tags necessarias 
    wanted_keys = set(['grup-nom-fs', 'grup-nom-fp', 'grup-nom-ms', 'grup-nom-mp'])
    #percorre as tags do ficheiro json
    for data in jsonObject['jsonfile']:
        for sentence in data['sentences']:
            for constituent in sentence['constituents']:
                for child in constituent['children']:
                    if 'label' in child:
                        #se existe logo na primeira children
                        if child['label'] in wanted_keys: 
                            loop0 = child 
                            wanted_list.append(loop0)
                        else:  
                            for labeltree in child['children']:
                                if 'label' in labeltree and labeltree['label'] in wanted_keys: #verifica se existe na segunda children
                                    loop1 = labeltree
                                    wanted_list.append(loop1)

                                else: #verifica se existe em todas a children
                                    loop2 = labeltree
                                    while ('word' in loop2) is False:
                                        for loop2 in loop2['children']:

                                            if 'label' in loop2 and loop2['label'] in wanted_keys:
                                                wanted_list.append(loop2)
                                                break
                                     
                                    #verifica se é a frase de quebra
                                    if 'word' in loop2 and loop2[
                                    'word'] == '----------------------------------------------------------------------------------------------':
                                        wanted_list.append('break here')
                                    
                    elif 'word' in child and child['word'] == '----------------------------------------------------------------------------------------------':                                    
                        wanted_list.append('break here')

             
    filter_list(wanted_list, nomeFicheiro)


def filter_list(list, nomeFicheiro): #filtra a lista que contem os objetos json
    word_fil = [] #lista de palavras filtradas
    for each in list:
        
        each = str(each)
        if 'break here' in each: #verifica se é uma quebra de frase
            word_fil.append('break here')

        else: #encontra as palavras
            count = 0 
            for m in re.finditer('word', each): #encontra a posiçao das 'word'
                word = ''

                i = 0
                while each[m.end() + 4 + i] != "'": #obtem a palavra através da posição da 'word'
                    word += each[m.end() + 4 + i]

                    i += 1

                if count == 1: #verifica se é mais do que uma palavra

                    word_fil[-1] = str(word_fil[-1]) + ' ' + word
                else:
                    word_fil.append(word)

                count = 1                     
       
        
    #criação de uma lista com strings separadas por ficheiro
    string = ''
    array_string = []
    for word in word_fil:
        if word == 'break here':
            array_string.append(string)
            string = ''
        else:
            string += word + '\n'

    array_string.append(string)

    n = 1
        
        
    nomeFicheiro = nomeFicheiro.replace(".json", "")
    for string in array_string:
           
        dic = word_count(string) #criação de um dicionario com o somatorio 
        
        with open(nomeFicheiro + '_' + str(n) + '_lexed.txt', 'w', encoding='utf-8') as f:
            for key, value in dic.items():
                f.write('%s \t %s\n' % (key,value) )
        n += 1





def word_count(string):
    counts = dict()
    words = string.split('\n')
    for word in words:
        if word != '':
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1      
    return counts
    
    



for nomeFicheiro in sys.argv[1:]:

    with open(nomeFicheiro, "r", encoding='utf-8') as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()


    search_words(jsonObject, nomeFicheiro)

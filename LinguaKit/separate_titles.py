#!/usr/bin/env python3

import sys
import re

#separa o ficheiro pelos titulos
for nomeFicheiro in sys.argv[1:]:

    aux = 0 
    aux2 = 0
    aux4 = 0

    file = open(nomeFicheiro, "r", encoding='utf8')
    sentences = file.readlines()
    file.close()

    title1 = []
    title2 = []
    title4 = []

    for sentence in sentences:
        words = sentence.split()
        for word in words:
            more_words = re.split(r"[<;:*/\"().,?]", word)


            #Le na linha asseguir ao <\title>
            if aux == 2: 
                aux = 3
            if aux2 == 2:
                aux2 = 3
            if aux4 == 2:
                aux4 = 3


            if 'title>4' in more_words:
                aux4 = 1
            elif 'title>' in more_words and aux4 == 1:
                aux4 = 2
            elif 'title>5' in more_words:
                aux4 = 0

            if 'title>2' in more_words:
                aux2 = 1
            elif 'title>' in more_words and aux2 == 1:
                aux2 = 2
            elif 'title>3' in more_words:
                aux2 = 0

            if 'title>1' in more_words:
                aux = 1
            elif 'title>' in more_words and aux == 1:
                aux = 2
            elif 'title>2' in more_words:
                aux = 0



        if aux == 3:
            title1.append(sentence)

        if aux2 == 3:
            title2.append(sentence)

        if aux4 == 3:
            title4.append(sentence)

    
    if not title1 and not title2 and not title4: #verifica se as listas estão vazias 
    	
        print('não encontrei nenhum componente')
    
    else:
        nomeFicheiro = nomeFicheiro.replace('.txt', '')	
    	
        if title1:
            file_to_be = open(nomeFicheiro + '_title1.txt', "w+")
            
            for each in title1:
            
                file_to_be.write(each + "\n")
            file_to_be.close()

        if title2:
            file_to_be2 = open(nomeFicheiro + '_title2.txt', "w+")
            for each in title2:
                file_to_be2.write(each + '\n')
            file_to_be2.close()
    	     	    
        if title4:
            file_to_be4 = open(nomeFicheiro + '_title4.txt', "w+")
            for each in title4:
    	        file_to_be4.write(each + '\n')
            file_to_be4.close()

    sentences.clear()
    title1.clear()
    title2.clear()
    title4.clear()

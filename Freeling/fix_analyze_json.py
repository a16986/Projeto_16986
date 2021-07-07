#!/usr/bin/env python3
import sys
import json
import re
import os
import os.path

#repara ficheiros json obtido do freeling
for nomeFicheiro in sys.argv[1:]:
    num = 0

    with open(nomeFicheiro, "r", encoding='utf-8') as file:
        jstring = file.read()

    #string responsavel por criar um novo objeto que possui como array todos os outros objetos
    jstring = re.sub(r'{\s"sentences"\s:\s\[\n\s{6}{\s"id":"1"', '{ "jsonfile" : [ \n { "sentences" : [\n\t{ "id":"1"',
                     jstring)


    #include uma virgula no final de cada objeto para indicar que não é o ultimo 
    jstring = re.sub(r']}]}]}', ']}]}]},', jstring)


    #transforma a string numa lista
    list_string = list(jstring)

    #a partir da lista obtenho a sua length
    i = len(list_string) - 1

    #a partir da length percorro o array top-down para encontrar o ultimo carater ',' que vai ser obtido do passo anterior
    while list_string[i] != ',':
        i = i - 1

    #apos obter a posição do ultimo carater troco-o por um ']}' para fechar o objeto
    list_string[i] = ']'
    list_string[i + 1] = '}'

    new_string = ''

    #apenas transforma a lista numa string novamente
    for letter in list_string:
        new_string += letter


    #processa o ficheiro
    if os.path.isfile('fixed_' + sys.argv[1]):
    	os.remove('fixed_' + sys.argv[1])
    with open('fixed_' + sys.argv[1], "w", encoding='utf-8') as outfile:
        json.dump(json.loads(new_string, strict = False ), outfile, indent="", ensure_ascii=False)

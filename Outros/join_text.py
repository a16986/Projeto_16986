#!/usr/bin/env python3

import sys


file = open(sys.argv[1], "w+")
if  file != -1: #verifica se o ficheiro existe e apaga-o se sim
	file.truncate(0)		
file.close	

n = 0 #serve para verificar se o ficheiro é o primeiro a ser lido
			
for nomeFicheiro in sys.argv[2:]:
	with open(nomeFicheiro, "r") as sourceFile:
		with open(sys.argv[1], "a") as targetFile:
			if n == 1:
				targetFile.write('\n\n----------------------------------------------------------------------------------------------\n\n')
			n = 1 #indica que o primeiro ja passou
			
			contents = sourceFile.read()
			targetFile.write(contents)
                    		




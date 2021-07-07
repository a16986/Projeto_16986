#!/usr/bin/env python3 

import sys
import os   


for nomeFicheiro in sys.argv[1:]:

			
	final_file = nomeFicheiro.replace(".txt","") + '.json'

	command = 'analyze --flush --outlv parsed --output json -f pt.cfg <' + nomeFicheiro + '>' + final_file
	
	os.system(command)

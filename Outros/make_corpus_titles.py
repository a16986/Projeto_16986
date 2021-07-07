#!/usr/bin/env python3

import sys
	
list1 = []
list2 = []
list4 = []

#faz o corpus a ser utilizado no kmeans através dos varios ficheiros lhe dados
for nomeFicheiro in sys.argv[1:]:

    with open(nomeFicheiro, "r") as f:
       	sentences = f.readlines()
       	f.close()
       	
    for sentence in sentences:
	    if '_title1' in sentence:
	        list1.append(sentence)
	    elif '_title2' in sentence: 
	        list2.append(sentence)
	    elif '_title4' in sentence: 
	        list4.append(sentence)

    with open('title1', 'w') as f:
        for each in list1:
            f.write(str(each) + '\n')  
        f.close()
 
    with open('title2', 'w') as f:
        for each in list2:
            f.write(str(each) + '\n')
        f.close()
        
    with open('title4', 'w') as f:
        for each in list4:
            f.write(str(each) + '\n')
        f.close()
       
	    

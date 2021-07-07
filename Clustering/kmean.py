#!/usr/bin/env python3
import sys
import nltk
import numpy as np
import re
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt #para fazer o plot
import pandas as pd


def process_text(list):
    string = ''
    liste = []
    for sentence in sentence_list:
        for word in sentence.split():
            if word.lower() not in stopwords.words('portuguese') and len(word) > 1:
                string += word + ' '
        liste.append(string)
        string = ''
        


    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~ •\n"
    for i in symbols:
        liste = np.char.replace(liste, i, ' ')


def get_top_keywords(k, km, terms):
   

    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    
    n = 0
    
    for i in range(k):
        print("Cluster %d:" % i, end = '')
        for ind in order_centroids[i, :10]:
            print(" %s" %terms[ind], end= '')
        print()


def find_optimal_clusters(data, max_k):
    iters = range(2, max_k+1, 2)
    
    sse = []
    for k in iters:
        #sum squared error
        sse.append(KMeans(n_clusters=k, random_state=20).fit(data).inertia_)
        print('Fit {} clusters'.format(k))
     
       
    f, ax = plt.subplots(1, 1)
    ax.plot(iters, sse, marker='o')
    ax.set_xlabel('Cluster Centers')
    ax.set_xticks(iters)
    ax.set_xticklabels(iters)
    ax.set_ylabel('SSE')
    ax.set_title('SSE by Cluster Center Plot')
    plt.show()



nltk.download('stopwords')



sentence_list = []
n = 0
nomes = []

with open(sys.argv[1], 'r', encoding = 'utf8') as file:
    sentences = file.readlines()
    file.close()


for files in sentences:
    nomes.append(files.replace('\n',''))
    n += 1
    with open(files.replace('\n',''), 'r', encoding = 'utf8') as f:
        file_sentences = f.readlines()
        f.close()


   
    sentence_list.append("".join(file_sentences))
    

sentences.clear()




string = ''
liste = []
for sentence in sentence_list:
    for word in sentence.split():
        if word.lower() not in stopwords.words('portuguese') and len(word) > 1:
            string += word + ' '
    liste.append(string)
    string = ''
  
sentence_list.clear()
      
#retira as palavras stopw<ords da lista de strings e palavras de tamanho 1
#retira simbolos
symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~ •\n"
for i in symbols:
    liste = np.char.replace(liste, i, ' ')
                
vectorizer=TfidfVectorizer(min_df= 5, max_df=0.95, decode_error='ignore')


v=vectorizer.fit(liste) #obtem o vocabulario e os falores idf
vectorized = v.transform(liste) 

print(pd.DataFrame(vectorized.toarray(), columns = vectorizer.get_feature_names())) #apresenta a matrix idf

find_optimal_clusters(vectorized, 60) 

km = KMeans(n_clusters=52, random_state=0)

clusters = km.fit_predict(vectorized)


get_top_keywords(52, km, vectorizer.get_feature_names())


results = pd.DataFrame()
results['text'] = nomes
results['category'] = km.labels_
print(results)

i = 0

dic_clusters = {}

for cluster in clusters:
        dic_clusters[re.sub(r'_title.*','',nomes[i])] = cluster
        i += 1
        

dic_clusters = sorted(dic_clusters.items(), key =lambda x:x[1])



temp = -1
with open("clusters " + sys.argv[1] , "w") as f:
    for key,value in dic_clusters:

    	if value != temp:
    		temp = value
    		f.write(str(value) + ':\n')
    	f.write(key + '\n') 

    f.close()
nomes.clear()

         
        
        
 

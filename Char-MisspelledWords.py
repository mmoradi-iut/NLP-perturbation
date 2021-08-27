import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

from builtins import str

import csv
import sys, getopt

import xml.etree.ElementTree as ET
from xml.dom.minidom import parse, Node
import xml.dom.minidom       
from numpy import double

from random import seed
from random import randint

seed(1)

#--------------------------------------------------------------------------------------------------------------------

def return_random_number(begin, end):
    return randint(begin, end)

#--------------------------------------------------------------------------------------------------------------------

max_perturb = 3

input_address = 'Dataset\\TREC.tsv'

output_text = 'text' + '\t' + 'label' + '\n'

num_perturbed_samples = 0
    
with open(input_address) as input_file:
        
    input_data = csv.reader(input_file, delimiter='\t')
    
    line_num = 0
    
    for row in input_data:
        
        if (line_num > 0):
        
            print(row[0], '\t', row[1])
        
            is_sample_perturbed = False
            
            sample_text = row[0]
            sample_label = row[1]
            sample_tokenized = nltk.word_tokenize(sample_text)
            
            #--------------------------- search in the misspelled words corpus
            
            corpus_address = 'Corpus\\MisspelledWords.tsv'
            
            perturbed_sample = ""
            word_replaced = False
            
            possible_misspelling = []
            
            with open(corpus_address) as corpus_file:
                corpus_data = csv.reader(corpus_file, delimiter='\t')
                
                
                #----- find all possible misspellings
                for entry in corpus_data:
                    
                    misspelling_position = sample_text.find(entry[0])
                    
                    if (misspelling_position > -1):
                        print('Can be replaced:', entry[0], '----- Misspelling:', entry[1])
                        possible_misspelling.append(entry)
                        
                
                if (len(possible_misspelling) > 0):
                    
                    #----- create a list of unique words in the sample that can be replaced by a misspelling
                    unique_words = []
                    for i in range(0, len(possible_misspelling)):
                        temp_row = possible_misspelling[i]
                        if (temp_row[0] not in unique_words):
                            unique_words.append(temp_row[0])
                            
                    print('Unique words that can be replaced with a misspelling:', unique_words, '\n')
                    num_unique_words = len(unique_words)
                    
                    #----- randomly choose a misspelling and perturb the sample
                    num_replacements = 0
                    already_replaced = []
                    
                    perturbed_sample = sample_text
                    
                    while (num_replacements < max_perturb and num_replacements < num_unique_words):
                        
                        random_index = return_random_number(0, len(possible_misspelling)-1)
                        temp_row = possible_misspelling[random_index]
                        
                        if (temp_row[0] not in already_replaced):
                            print(temp_row[0], 'is replaced with', temp_row[1])
                            misspelling_position = perturbed_sample.find(temp_row[0])
                            
                            temp_text = perturbed_sample[0:misspelling_position]
                            temp_text += temp_row[1]
                            temp_text += perturbed_sample[misspelling_position+len(temp_row[0]):]
                            
                            perturbed_sample = temp_text
                            
                            already_replaced.append(temp_row[0])
                            word_replaced = True
                            
                            num_replacements += 1
                        
                        
                        
            if (word_replaced == False):
                print('No misspelled word was replaced')    
                perturbed_sample = sample_text
                
            if (word_replaced == True):
                is_sample_perturbed = True
                num_perturbed_samples += 1
                    
            
            print('Perturbed sample:', perturbed_sample)
            
            if (is_sample_perturbed == True):
                output_text += perturbed_sample + '\t' + sample_label + '\n'
        
            print('----------------------------------------------------------')
        line_num += 1
        
        
print('\nPerturbed Samples:', num_perturbed_samples)

output_file = open('Dataset\\TREC-perturbed-char-misspelled-words.tsv', 'w')
output_file.write(output_text)
output_file.close()
        


if __name__ == '__main__':
    pass
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

def change_ordering(input_length, input_side, input_changes):
    ordering = []
    
    if (input_side == 1):
        for i in range(0, input_length):
            if (i < input_changes):
                
                candidates=[]
                for j in range(0, input_changes):
                    if (j != i and j not in ordering):
                        candidates.append(j)
                        
                if (len(candidates) > 0):
                    random_index = return_random_number(0, len(candidates)-1)
                    ordering.append(candidates[random_index])
                else:
                    ordering.append(i)
            else:
                ordering.append(i)
                
    elif (input_side == 2):
        for i in range(0, input_length):
            if (i < input_length-input_changes):
                ordering.append(i)
                
            else:
                candidates=[]
                for j in range(input_length-input_changes, input_length):
                    if (j != i and j not in ordering):
                        candidates.append(j)
                        
                if (len(candidates) > 0):
                    random_index = return_random_number(0, len(candidates)-1)
                    ordering.append(candidates[random_index])
                else:
                    ordering.append(i)
                        
    return ordering
        

#--------------------------------------------------------------------------------------------------------------------

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
        
            random_word_index = 0
            random_word_selected = False
            
            perturbed_sample = ""
            
            if (len(sample_tokenized) > 3):
                print('Sample can be perturbed.')
                
                last_token = ""
                if (sample_tokenized[len(sample_tokenized)-1] in ('.', '?', '!', ';', ',')):
                    last_token = sample_tokenized[len(sample_tokenized)-1]
                    sample_tokenized = sample_tokenized[0: len(sample_tokenized)-1]
                
                ordering_side = return_random_number(1, 2)
                
                if (ordering_side == 1): #----- change word ordering in the beginning
                    print('Change ordering side: Beginning')
                elif (ordering_side == 2): #----- change word ordering in the end
                    print('Change ordering side: End')
                    
                num_changed_words = return_random_number(2, len(sample_tokenized)-1)
                print('Number of words for changing the order:', num_changed_words)
                    
                new_word_order = change_ordering(len(sample_tokenized), ordering_side, num_changed_words)
                    
                print('New word order:', new_word_order)
                
                for i in range(0, len(new_word_order)):
                    temp_index = new_word_order[i]
                    perturbed_sample += sample_tokenized[temp_index] + ' '
                perturbed_sample += last_token
                
                num_perturbed_samples += 1
                is_sample_perturbed = True
                
            else:
                perturbed_sample = sample_text
            
            
            print('Perturbed sample:', perturbed_sample)
            
            if (is_sample_perturbed == True):
                output_text += perturbed_sample + '\t' + sample_label + '\n'
        
            print('----------------------------------------------------------')
        line_num += 1
        
        
print('Perturbed samples:', num_perturbed_samples)

output_file = open('Dataset\\TREC-perturbed-word-ordering.tsv', 'w')
output_file.write(output_text)
output_file.close()
        


if __name__ == '__main__':
    pass
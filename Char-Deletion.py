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

input_address = 'Dataset\\TREC.tsv'

output_text = 'text' + '\t' + 'label' + '\n'
    
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
        
            while (random_word_selected != True):
                random_word_index = return_random_number(0, len(sample_tokenized)-1)
                if (len(sample_tokenized[random_word_index]) > 2):
                    random_word_selected = True
        
            print('Selected random word:', sample_tokenized[random_word_index])
            
            #--------------------------- select a random position
            
            selected_word = sample_tokenized[random_word_index]
            
            random_char_index = return_random_number(1, len(selected_word)-2)
            print('Random position:', random_char_index)
            print('Character to delete:', selected_word[random_char_index])
            
            #--------------------------- delete the character
        
            temp_word = selected_word[:random_char_index]
            temp_word += selected_word[random_char_index+1:]
            
            perturbed_word = ""
            for i in range(0, len(temp_word)):
                perturbed_word += temp_word[i]
            
            print('After deletion:', perturbed_word)
            
            #--------------------------- reconstruct the perturbed sample
            
            perturbed_sample = ""
            
            for i in range(0, random_word_index):
                    
                perturbed_sample += sample_tokenized[i] + ' '
                
            perturbed_sample += perturbed_word + ' '
            is_sample_perturbed = True
            
            for i in range(random_word_index+1, len(sample_tokenized)):    
                perturbed_sample += sample_tokenized[i] + ' '
            
            print('Perturbed sample:', perturbed_sample)
            
            if (is_sample_perturbed == True):
                output_text += perturbed_sample + '\t' + sample_label + '\n'
        
            print('----------------------------------------------------------')
        line_num += 1
        
        
output_file = open('Dataset\\TREC-perturbed-char-deletion.tsv', 'w')
output_file.write(output_text)
output_file.close()
        


if __name__ == '__main__':
    pass
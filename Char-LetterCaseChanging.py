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

def random_changing_type():
    random_num = randint(1, 2)
    if (random_num == 1):
        return 'FirstChar'
    else:
        return 'AllChars'

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
            
            #--------------------------- select the type of letter case changing
            
            selected_word = sample_tokenized[random_word_index]
            
            temp_word = ""
            
            change_type = random_changing_type()
            
            #--------------------------- change the letter case
            
            if (change_type == 'FirstChar'):
                print('Letter case changing: First character')
                if (ord(selected_word[0]) >= 97 and ord(selected_word[0]) <= 122):
                    temp_word = chr(ord(selected_word[0])-32)
                    temp_word += selected_word[1:]
                    is_sample_perturbed = True
                elif (ord(selected_word[0]) >= 65 and ord(selected_word[0]) <= 90):
                    temp_word = chr(ord(selected_word[0])+32)
                    temp_word += selected_word[1:]
                    is_sample_perturbed = True
                else:
                    temp_word = selected_word
                    
            elif (change_type == 'AllChars'):
                print('Letter case changing: All characters')
                for i in range(0, len(selected_word)):
                    if (ord(selected_word[i]) >= 97 and ord(selected_word[i]) <= 122):
                        temp_word += chr(ord(selected_word[i])-32)
                        is_sample_perturbed = True
                    elif (ord(selected_word[i]) >= 65 and ord(selected_word[i]) <= 90):
                        temp_word += chr(ord(selected_word[i])+32)
                        is_sample_perturbed = True
                    else:
                        temp_word += selected_word[i]
            
            
            
            perturbed_word = ""
            for i in range(0, len(temp_word)):
                perturbed_word += temp_word[i]
            
            print('After letter case changing:', perturbed_word)
            
            #--------------------------- reconstruct the perturbed sample
            
            perturbed_sample = ""
            
            for i in range(0, random_word_index):
                    
                perturbed_sample += sample_tokenized[i] + ' '
                
            perturbed_sample += perturbed_word + ' '
            
            for i in range(random_word_index+1, len(sample_tokenized)):    
                perturbed_sample += sample_tokenized[i] + ' '
            
            print('Perturbed sample:', perturbed_sample)
            
            if (is_sample_perturbed == True):
                output_text += perturbed_sample + '\t' + sample_label + '\n'
        
            print('----------------------------------------------------------')
        line_num += 1
        
        
output_file = open('Dataset\\TREC-perturbed-char-letter-case-changing.tsv', 'w')
output_file.write(output_text)
output_file.close()
        


if __name__ == '__main__':
    pass
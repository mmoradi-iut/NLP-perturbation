import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

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

def return_adjacent_char(input_char):
    
    if (input_char == 'a'):
        return 's'
    
    elif (input_char == 'b'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'v'
        else:
            return 'n'
        
    elif (input_char == 'c'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'x'
        else:
            return 'v'
        
    elif (input_char == 'd'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 's'
        else:
            return 'f'
        
    elif (input_char == 'e'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'w'
        else:
            return 'r'
        
    elif (input_char == 'f'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'd'
        else:
            return 'g'
        
    elif (input_char == 'g'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'f'
        else:
            return 'h'
        
    elif (input_char == 'h'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'g'
        else:
            return 'j'
        
    elif (input_char == 'i'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'u'
        else:
            return 'o'
        
    elif (input_char == 'j'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'h'
        else:
            return 'k'
        
    elif (input_char == 'k'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'j'
        else:
            return 'l'
    
    elif (input_char == 'l'):
        return 'k'
        
    elif (input_char == 'm'):
        return 'n'
        
    elif (input_char == 'n'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'b'
        else:
            return 'm'
        
    elif (input_char == 'o'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'i'
        else:
            return 'p'
        
    elif (input_char == 'p'):
        return 'o'
    
    elif (input_char == 'q'):
        return 'w'
        
    elif (input_char == 'r'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'e'
        else:
            return 't'
        
    elif (input_char == 's'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'a'
        else:
            return 'd'
        
    elif (input_char == 't'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'r'
        else:
            return 'y'
        
    elif (input_char == 'u'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'y'
        else:
            return 'i'
    
    elif (input_char == 'v'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'c'
        else:
            return 'b'
        
    elif (input_char == 'w'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'q'
        else:
            return 'e'
        
    elif (input_char == 'x'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'z'
        else:
            return 'c'
        
    elif (input_char == 'y'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 't'
        else:
            return 'u'
        
    elif (input_char == 'z'):
        return 'x'
    #---------------------------------------------
    elif (input_char == 'A'):
        return 'S'
    
    elif (input_char == 'B'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'V'
        else:
            return 'N'
        
    elif (input_char == 'C'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'X'
        else:
            return 'V'
        
    elif (input_char == 'D'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'S'
        else:
            return 'F'
        
    elif (input_char == 'E'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'W'
        else:
            return 'R'
        
    elif (input_char == 'F'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'D'
        else:
            return 'G'
        
    elif (input_char == 'G'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'F'
        else:
            return 'H'
        
    elif (input_char == 'H'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'G'
        else:
            return 'J'
        
    elif (input_char == 'I'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'U'
        else:
            return 'O'
        
    elif (input_char == 'J'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'H'
        else:
            return 'K'
        
    elif (input_char == 'K'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'J'
        else:
            return 'L'
    
    elif (input_char == 'L'):
        return 'K'
        
    elif (input_char == 'M'):
        return 'N'
        
    elif (input_char == 'N'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'B'
        else:
            return 'M'
        
    elif (input_char == 'O'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'I'
        else:
            return 'P'
        
    elif (input_char == 'P'):
        return 'O'
    
    elif (input_char == 'Q'):
        return 'W'
        
    elif (input_char == 'R'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'E'
        else:
            return 'T'
        
    elif (input_char == 'S'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'A'
        else:
            return 'D'
        
    elif (input_char == 'T'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'R'
        else:
            return 'Y'
        
    elif (input_char == 'U'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'Y'
        else:
            return 'I'
    
    elif (input_char == 'V'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'C'
        else:
            return 'B'
        
    elif (input_char == 'W'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'Q'
        else:
            return 'E'
        
    elif (input_char == 'X'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'Z'
        else:
            return 'C'
        
    elif (input_char == 'Y'):
        which_adjacent = return_random_number(1, 2)
        if (which_adjacent == 1):
            return 'T'
        else:
            return 'U'
        
    elif (input_char == 'Z'):
        return 'X'
    
    else:
        return '*'

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
            
            char_is_letter = False
            tries_number = 0
            
            while (char_is_letter != True and tries_number <= 20):
                random_char_index = return_random_number(1, len(selected_word)-2)
                tries_number += 1
                if ((ord(selected_word[random_char_index]) >= 97 and ord(selected_word[random_char_index]) <= 122) or (ord(selected_word[random_char_index]) >= 65 and ord(selected_word[random_char_index]) <= 90)):
                    char_is_letter = True
                    is_sample_perturbed = True
            
            
            print('Random position:', random_char_index)
            print('Character to replace:', selected_word[random_char_index])
            
            #--------------------------- replace the character
        
            char_to_replace = selected_word[random_char_index]
            
            adjacent_char = return_adjacent_char(char_to_replace)
            
            print('Adjacent character:', adjacent_char)
            
            temp_word = selected_word[:random_char_index]
            temp_word += adjacent_char
            temp_word += selected_word[random_char_index+1:]
            
            perturbed_word = ""
            for i in range(0, len(temp_word)):
                perturbed_word += temp_word[i]
            
            print('After replacement:', perturbed_word)
            
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
        
        
output_file = open('Dataset\\TREC-perturbed-char-replacement.tsv', 'w')
output_file.write(output_text)
output_file.close()
        


if __name__ == '__main__':
    pass
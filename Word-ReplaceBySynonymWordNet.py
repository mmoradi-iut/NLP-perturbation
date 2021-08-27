import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('wordnet')

from builtins import str

import csv
import sys, getopt

import xml.etree.ElementTree as ET
from xml.dom.minidom import parse, Node
import xml.dom.minidom       
from numpy import double

from random import seed
from random import randint

from nltk.corpus import wordnet


seed(1)

#--------------------------------------------------------------------------------------------------------------------

def return_random_number(begin, end):
    return randint(begin, end)


class Synonym:
    
    def __init__(self, first_word, second_word):
        self.first_word = first_word
        self.second_word = second_word

#--------------------------------------------------------------------------------------------------------------------


max_replace = 3

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
            sample_pos_tag = nltk.pos_tag(sample_tokenized)
        
            word_replaced = False
            perturbed_sample = sample_text
            
            candidate_synonym = []
            can_be_replaced_list = []
            
            for i in range(0, len(sample_pos_tag)):
                if (sample_pos_tag[i][1] in ('CD', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'RB', 'RBR', 'RBS')): #----- Replace the word if it is a noun, adjective, or adverb
                    for syn in wordnet.synsets(sample_pos_tag[i][0]):
                        for l in syn.lemmas():
                            if (sample_pos_tag[i][0] != l.name()):
                                temp_synonym = Synonym(sample_pos_tag[i][0], l.name())
                                candidate_synonym.append(temp_synonym)
                                if (sample_pos_tag[i][0] not in can_be_replaced_list):
                                    can_be_replaced_list.append(sample_pos_tag[i][0])
            
                    
            if (len(candidate_synonym) > 0):
                print('Words that can be replaced:', can_be_replaced_list)
                
                unique_words = len(can_be_replaced_list)
                num_perturbed_words = 0
                
                
                index = 0
                while (num_perturbed_words < max_replace and num_perturbed_words < unique_words):
                    possible_replacement = []
                    
                    for i in range(0, len(candidate_synonym)):
                        if (candidate_synonym[i].first_word == can_be_replaced_list[index] or candidate_synonym[i].second_word == can_be_replaced_list[index]):
                            possible_replacement.append(candidate_synonym[i])
                            
                            
                    random_candidate = return_random_number(0, len(possible_replacement)-1)
                    
                    original_word = ''
                    new_word = ''
                    if (possible_replacement[random_candidate].first_word == can_be_replaced_list[index]):
                        original_word = possible_replacement[random_candidate].first_word
                        new_word = possible_replacement[random_candidate].second_word
                    elif (possible_replacement[random_candidate].second_word == can_be_replaced_list[index]):
                        original_word = possible_replacement[random_candidate].second_word
                        new_word = possible_replacement[random_candidate].first_word
                        
                    print(original_word, 'is replaced by', new_word)
                    
                    perturbed_sample_tokenized = nltk.word_tokenize(perturbed_sample)
                    replacement_position = -1
                    for i in range(0, len(perturbed_sample_tokenized)):
                        if (original_word == perturbed_sample_tokenized[i]):
                            replacement_position = i
                            
                    if (replacement_position > -1):
                        perturbed_sample = ""
                        for i in range(0, replacement_position):
                            perturbed_sample += perturbed_sample_tokenized[i] + ' '
                        perturbed_sample += new_word + ' '
                        for i in range(replacement_position+1, len(perturbed_sample_tokenized)):
                            perturbed_sample += perturbed_sample_tokenized[i] + ' '
                    
                        word_replaced = True
                        num_perturbed_words += 1
                        
                        
                    index += 1
                    
            elif (len(candidate_synonym) == 0):
                print('No word was replaced.')
        
            
            if (word_replaced == True):
                is_sample_perturbed = True
                num_perturbed_samples += 1
            
            print('Perturbed sample:', perturbed_sample)
            
            if (is_sample_perturbed == True):
                output_text += perturbed_sample + '\t' + sample_label + '\n'
            
        
            print('----------------------------------------------------------')
        line_num += 1
        
        
print('\nPerturbed Samples:', num_perturbed_samples)

output_file = open('Dataset\\TREC-perturbed-word-replace-synonym-wordnet.tsv', 'w')
output_file.write(output_text)
output_file.close()
        


if __name__ == '__main__':
    pass
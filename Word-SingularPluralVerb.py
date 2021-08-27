import nltk
nltk.download('averaged_perceptron_tagger')
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
import mlconjug3

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
            sample_pos_tag = nltk.pos_tag(sample_tokenized)
            
            print(sample_pos_tag)
            
            Perturbed_sample = ""
            
            remove_negation = False
            
            for i in range(0, len(sample_pos_tag)):
                token = sample_pos_tag[i]
                print(token[0], token[1])
                if (remove_negation == False):
                    if (token[0] == 'has' and sample_pos_tag[i+1][1] == 'VBN'): #----- third person singular present perfect
                        verb = 'have'
                        Perturbed_sample += verb + ' '
                        is_sample_perturbed = True
                    
                    elif (token[0] == 'have' and sample_pos_tag[i+1][1] == 'VBN'): #----- present perfect
                        verb = 'has'
                        Perturbed_sample += verb + ' '
                        is_sample_perturbed = True
                    
                    elif (token[0] == 'does' and sample_pos_tag[i+1][0] in ('not', "n't")): #----- negative, third person present simple
                        verb = 'do not'
                        remove_negation = True
                        Perturbed_sample += verb + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'do' and sample_pos_tag[i+1][0] in ('not', "n't")): #----- negative, present simple
                        verb = 'does not'
                        remove_negation = True
                        Perturbed_sample += verb + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'has' and sample_pos_tag[i+1][0] in ('not', "n't")): #----- negative, third person present perfect
                        remove_negation = True
                        Perturbed_sample += "have not" + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'have' and sample_pos_tag[i+1][0] in ('not', "n't")): #----- negative, present perfect
                        remove_negation = True
                        Perturbed_sample += "has not" + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'is' and sample_pos_tag[i+1][0] in ('not', "n't")): #----- negative, to be present and past, continuous present and past
                        remove_negation = True
                        Perturbed_sample += 'are not' + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'are' and sample_pos_tag[i+1][0] in ('not', "n't")): #----- negative, to be present and past, continuous present and past
                        remove_negation = True
                        Perturbed_sample += 'is not' + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'was' and sample_pos_tag[i+1][0] in ('not', "n't")): #----- negative, to be present and past, continuous present and past
                        remove_negation = True
                        Perturbed_sample += 'were not' + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'were' and sample_pos_tag[i+1][0] in ('not', "n't")): #----- negative, to be present and past, continuous present and past
                        remove_negation = True
                        Perturbed_sample += 'was not' + ' '
                        is_sample_perturbed = True
                    
                    elif (token[0] == 'does'): #----- negative, third person present simple
                        verb = 'do'
                        Perturbed_sample += verb + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'do'): #----- negative, present simple
                        verb = 'does'
                        Perturbed_sample += verb + ' '
                        is_sample_perturbed = True
                    
                    elif (token[0] == 'is'): #----- to be present and past, continuous present and past
                        Perturbed_sample += 'are' + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'are'): #----- to be present and past, continuous present and past
                        Perturbed_sample += 'is' + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'was'): #----- to be present and past, continuous present and past
                        Perturbed_sample += 'were' + ' '
                        is_sample_perturbed = True
                        
                    elif (token[0] == 'were'): #----- to be present and past, continuous present and past
                        Perturbed_sample += 'was' + ' '
                        is_sample_perturbed = True
                
                    elif (token[1] == 'VBZ'): #----- third person singular present
                        verb = token[0]
                        length = len(verb)
                        if (verb == 'has'):
                            verb = 'have'
                        elif (verb[length-3:] == 'oes'):
                            verb = verb[:length-2]
                        elif (verb[length-4:] == 'ches'):
                            verb = verb[:length-2]
                        elif (verb[length-3:] == 'ses'):
                            verb = verb[:length-2]
                        elif (verb[length-4:] == 'shes'):
                            verb = verb[:length-2]
                        elif (verb[length-3:] == 'xes'):
                            verb = verb[:length-2]
                        elif (verb[length-3:] == 'zes'):
                            verb = verb[:length-2]
                        elif (verb[length-3:] == 'ies'):
                            verb = verb[:length-3] + 'y'
                        else:
                            verb = verb[:length-1]
                        Perturbed_sample += verb + ' '
                        is_sample_perturbed = True
                    
                    elif (token[1] == 'VBP'): #----- basic form present
                        verb = token[0]
                        length = len(verb)
                        if (verb == 'have'):
                            verb = 'has'
                        elif (verb == 'go'):
                            verb = 'goes'
                        elif (verb[length-2:] == 'ch'):
                            verb = verb + 'es'
                        elif (verb[length-1:] == 's'):
                            verb = verb + 'es'
                        elif (verb[length-2:] == 'sh'):
                            verb = verb + 'es'
                        elif (verb[length-1:] == 'x'):
                            verb = verb + 'es'
                        elif (verb[length-1:] == 'z'):
                            verb = verb + 'es'
                        elif (verb[length-1:] == 'y'):
                            verb = verb[:length-1] + 'ies'
                        else:
                            verb = verb + 's'
                        Perturbed_sample += verb + ' '
                        is_sample_perturbed = True
                    
                    else:
                        Perturbed_sample += token[0] + ' '
                        
                elif (remove_negation == True):
                    if (token[0] in ('not', "n't")): #----- removing not after do or does
                        Perturbed_sample += ""
                        remove_negation = False
                        
            
            
            print('Perturbed sample:', Perturbed_sample)
            
            if (is_sample_perturbed == True):
                output_text += Perturbed_sample + '\t' + sample_label + '\n'
        
            print('----------------------------------------------------------')
        line_num += 1
        
        
output_file = open('Dataset\\TREC-perturbed-word-singularpluralverb.tsv', 'w')
output_file.write(output_text)
output_file.close()
        


if __name__ == '__main__':
    pass
# CS122: Auto-completing keyboard using Tries
#
# usage: python trie_dict.py <dictionary filename>
#
# Shrabya Timsina

import os
import sys
from sys import exit
import tty
import termios
import fcntl
import string

import trie_shell

def create_trie_node():
    """
    creates a new node for a trie
    returns: a dictionary with keys 'count' and 'final'
    """
    return {'count': 0, 'final' : False }

def add_word(word, trie):

    """
    adds a word to a given trie
    inputs: word - a string which contains the word to be added
            trie - a dictionary to which the word is added
    """
    trie['count'] += 1

    if word[0] not in trie: 
        trie[word[0]] = create_trie_node()

    
    if len(word) == 1:
        trie[word]['count'] = 1
        trie[word]['final'] = True
        return trie
    
    return add_word(word[1:], trie[word[0]])

    

def is_word(word, trie):
    """
    verifies if given word is a complete word in the given trie
    inputs: word - a string which contains the word to be verified
            trie - a dictionary to search through for given word

    returns - a boolean - stating whether the word is a complete word
    """ 

    if not word:
        return False

    elif word[0] not in trie:
        return False

    else: 

        if len(word) == 1:
            return trie[word]['final']

        return is_word(word[1:], trie[word[0]])

def num_completions(word, trie):
    # replace 0 with an appropriate value
    if not word:
        return trie['count']

    elif word[0] not in trie:
        return 0
   
    if len(word) == 1:

        return trie[word]['count']

    return num_completions(word[1:], trie[word[0]])

def get_completions(word, trie):
    # replace [] with an appropriate value
    prefix_trie = get_to_prefix_node(word, trie)

    if prefix_trie == None: #if prefix not in dictionary
        return []

    else:
        return complete_prefix(prefix_trie)

  
    

def get_to_prefix_node(word, trie):
    
    if not word: #check for empty string prefix
        return trie

    if word[0] not in trie:
        return None #if prefix not in dict or misspelled
    
    else:
        if len(word) == 1:
            return trie[word]

        return get_to_prefix_node(word[1:], trie[word[0]])

def complete_prefix(trie):
   

    if trie['final'] == True and trie['count'] == 1:
        return [""]

    else:
        completions_list = []

                
        exclude_keys = ['count', 'final']
        letters = [key for key in trie.keys() if key not in exclude_keys]
        
        if trie['count'] > 1 and trie['final'] == True:
            completions_list.append("") 
        
        for letter in letters:
       
            for leaf in complete_prefix(trie[letter]):

                completions_list.append(letter + leaf)

    
        return completions_list






if __name__ == "__main__":
    trie_shell.go("trie_dict")


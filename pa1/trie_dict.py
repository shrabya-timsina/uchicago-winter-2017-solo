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
        trie[word]['count'] += 1
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

    if not word: #case where word is an empty string
        return False

    elif word[0] not in trie: #if word not in dictionary or misspelled
        return False
     
    elif len(word) == 1:
        return trie[word]['final']

    return is_word(word[1:], trie[word[0]])

def num_completions(prefix, trie):
    """
    find number of full words beginning with given prefix
    including the prefix itself if it is a complete word
    
    inputs: prefix - a string which contains the prefix whose
                     number of completions are to be calculated
            trie - a dictionary to search through for completions count
    returns - an integer - value for the key 'count' for trie of given prefix
    """ 

    if not prefix: #case where prefix is an empty string
        return trie['count']

    elif prefix[0] not in trie: #if prefix not in dictionary or misspelled
        return 0

    if len(prefix) == 1:
        return trie[prefix]['count']

    return num_completions(prefix[1:], trie[prefix[0]])

def get_completions(prefix, trie):
    """
    find all suffixes of a specified prefix, which together
    represent a word in the trie
    
    inputs: prefix - a string which contains the prefix whose
                     word-forming suffixes are to be found
            trie - a dictionary to search through for valid suffixes
    returns - a list - containing all valid suffixes of the prefix
                       or empty list if there are no valif suffixes
    """ 
    #locating trie of prefix containing all possible suffixes
    prefix_trie = get_to_prefix_node(prefix, trie)

    if prefix_trie == None: #if prefix not in dictionary or misspelled
        return []

    else:
        return complete_prefix(prefix_trie)

def get_to_prefix_node(prefix, trie):
    """
    helper function to locate trie containing
    all possible suffixes within the larger trie
    """
    
    if not prefix: #case where prefix is an empty string 
        return trie

    if prefix[0] not in trie:
        return None #if prefix not in trie or misspelled
    
    else:
        if len(prefix) == 1:
            return trie[prefix]

        return get_to_prefix_node(prefix[1:], trie[prefix[0]])

def complete_prefix(trie):
    """
    helper function to find list of valid suffixes within
    the trie of the given prefix
    """
    # base case - leaf of dictionary i.e no sub-tries within
    if trie['final'] == True and trie['count'] == 1:
        return [""]  

    else:
        completions_list = []
        
        # case where suffix is not leaf but still a valid word
        if trie['count'] > 1 and trie['final'] == True:
            completions_list.append("")
                
        exclude_keys = ['count', 'final']
        #making list to  loop only through  keys that are letters
        letters = [key for key in trie.keys() if key not in exclude_keys]
        #case where there are subtries:                 
        for letter in letters:
            for leaf in complete_prefix(trie[letter]):
                completions_list.append(letter + leaf)
    
        return completions_list

if __name__ == "__main__":
    trie_shell.go("trie_dict")


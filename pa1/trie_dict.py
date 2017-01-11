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
    # replace None with an appropriate value
    return {'count': 0, 'final' : False }

def add_word(word, trie):
    # replace pass with your code
    
    trie['count'] += 1

    if word[0] not in trie: 
        trie[word[0]] = create_trie_node()

    if len(word) == 1:
        trie[word]['count'] = 1
        trie[word]['final'] = True
        return trie
    
    return add_word(word[1:], trie[word[0]])

    

def is_word(word, trie):
    # replace False with an appropriate value
    
    if len(word) == 1:
        return trie[word]['final']

    return is_word(word[1:], trie[word[0]])

def num_completions(word, trie):
    # replace 0 with an appropriate value

    if len(word) == 1:
        return trie[word]['count']

    return num_completions(word[1:], trie[word[0]])


def get_completions(word, trie):
    # replace [] with an appropriate value
    
   # completion_list = []

    

    if trie[word]['count'] == 1 and  trie[word]['final'] == True:
        completion_list.append(word)

    

def get_to_prefix_node(word, trie):
    
    if word[0] not in trie:
        return None #if prefix not in dict or misspelled
    
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

        for letter in letters:
            print("letter: ", letter)
            suffix = ""
            suffix = suffix + letter + complete_prefix(trie[letter])[0]
            print("suffix: ", suffix)
            completions_list.append(suffix)
            print("list: ", completions_list)

    
    return completions_list






   


    #letters_only = {letter: prefix[letter] for k in ('l', 'm', 'n')}
    
    #for letter in prefix.keys():






"""
if __name__ == "__main__":
    trie_shell.go("trie_dict")

"""
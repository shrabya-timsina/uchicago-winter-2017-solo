# CS122 W'17: Markov models and hash tables
# Shrabya Timsina 

TOO_FULL = 0.5
GROWTH_RATIO = 2

class Hash_Table:

    def __init__(self,cells,defval):
        '''
        Construct a bnew hash table with a fixed number of cells equal to the
        parameter "cells", and which yields the value defval upon a lookup to a
        key that has not previously been inserted
        '''
        assert cells > 0, \
            "number of cells must be positive"
        assert isinstance(cells, int), \
            "number of cells must be an integer"

        self.defval = defval
        self.table = [(None, None)] * cells #table is a list of (key, value) tuples
        self.num_of_keys = 0 

    def lookup(self,key):
        '''
        Retrieve the value associated with the specified key in the hash table,
        or return the default value if it has not previously been inserted.
        '''
        hash_val = self.hashing_function(key)
        
        #if index is unused skips while loop, returns defval
        #if index is used, proceeds down table until key is located or
        #until an unused cell is found - at which it point returns defval
        while self.table[hash_val][0] is not None:
            if self.table[hash_val][0] == key:
                return self.table[hash_val][1] 
            if hash_val == (len(self.table) -1):
                hash_val = -1 #to reset index to 0 after end has been reached
            hash_val = hash_val + 1
           
        return self.defval

    def update(self,key,val):
        '''
        Change the value associated with key "key" to value "val".
        If "key" is not currently present in the hash table,  insert it with
        value "val".
        '''
        hash_val = self.hashing_function(key)
        #if index is used, proceeds down table until key is located 
        #or  unused cell is found
        while self.table[hash_val][0] is not None:
                if self.table[hash_val][0] == key:
                    self.table[hash_val] = (key, val)
                    break 
                if hash_val == (len(self.table) - 1):
                    hash_val = -1 #to reset index to 0 after end has been reached
                hash_val = hash_val + 1

        #if initial hash_val index is unused or 
        #while loop finds adjacent unused cell, inserts key and value 
        if self.table[hash_val][0] is None:
            self.table[hash_val] = (key, val)
            self.num_of_keys += 1

        if (self.num_of_keys/len(self.table)) > TOO_FULL:
            self.rehash_after_full()
                
    def hashing_function(self, key):
        '''
        Finds a numeric value - the hash value - for an input string 'key'
        '''
        hash_val = 0
        for letter in key:
            hash_val = (hash_val*37) + ord(letter)
        hash_val = hash_val % len(self.table)
        return hash_val

    def rehash_after_full(self):
        '''
        doubles the size of the hash table after half its cells have been
        occupied and reinserts the existing keys into the hash table
        '''
        table_to_rehash = self.table[:]    
        self.table = [(None, None)] * len(self.table) * GROWTH_RATIO
        self.num_of_keys = 0 
        for key, val in table_to_rehash:
            if key is not None:
                self.update(key, val)


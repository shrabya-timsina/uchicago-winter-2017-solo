# CS122 W'17: Markov models and hash tables
# YOUR NAME HERE


TOO_FULL = 0.5
GROWTH_RATIO = 2


class Hash_Table:

    def __init__(self,cells,defval):
        '''
        Construct a bnew hash table with a fixed number of cells equal to the
        parameter "cells", and which yields the value defval upon a lookup to a
        key that has not previously been inserted
        '''
        ### YOUR CODE HERE ###
        self.defval = defval
        self.table = [None] * cells
        self.num_of_keys = 0 

    def lookup(self,key):
        '''
        Retrieve the value associated with the specified key in the hash table,
        or return the default value if it has not previously been inserted.
        '''
        hash_val = self.hashing_function(key)
        
        #if index is unused and key has not been inserted, returns defval
        if self.table[hash_val] is None:
            return self.defval

        #if index is used, proceeds down table until key is located or
        #until an unused cell is found - at which it point returns defval
        while self.table[hash_val] is not None:
            if self.table[hash_val][0] == key:
                return self.table[hash_val][1] #
            if hash_val == len(self.table):
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
        #if index is unused and key has not been inserted or if key exists 
        if (self.table[hash_val] is None):
            self.table[hash_val] = (key, val)
            self.num_of_keys += 1

        if self.table[hash_val][0] == key:
            self.table[hash_val] = (key, val)

        #if index is used, proceeds down table until unused cell is found
        else:
            while self.table[hash_val] is not None:
                if hash_val == len(self.table):
                    hash_val = -1 #to reset index to 0 after end has been reached
                hash_val = hash_val + 1

            self.table[hash_val] = (key, val)
            self.num_of_keys += 1

        if self.num_of_keys/len(self.table) > TOO_FULL:
            self.rehash_after_full()
                
    def hashing_function(self, key):
        hash_val = 0
        for letter in key:
            hash_val = (hash_val*37) + ord(letter)
        hash_val = hash_val % len(self.table)
        return hash_val

    def rehash_after_full(self):
        old_table = self.table[:]    
        self.table = [None] * len(self.table) * GROWTH_RATIO
        for item in old_table:
            if item is not None:
                self.update(item[0], item[1])




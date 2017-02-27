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
        self.defval = defval
        self.table = [(None, None)] * cells
        self.num_of_keys = 0 

    def lookup(self,key):
        '''
        Retrieve the value associated with the specified key in the hash table,
        or return the default value if it has not previously been inserted.
        '''
        hash_val = self.hashing_function(key)
        
        #if index is unused and key has not been inserted, returns defval
        if self.table[hash_val][0] is None:
            return self.defval

        #if index is used, proceeds down table until key is located or
        #until an unused cell is found - at which it point returns defval

        while self.table[hash_val][0] is not None:
            if self.table[hash_val][0] == key:
                return self.table[hash_val][1] #
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
        
        #if index is unused and key has not been inserted or if key exists 
        if self.table[hash_val][0] is None:
            self.table[hash_val] = (key, val)
            self.num_of_keys += 1

        elif self.table[hash_val][0] == key:
            self.table[hash_val] = (key, val)

        #if index is used, proceeds down table until unused cell is found
        else:
            
            while self.table[hash_val][0] is not None:
                #print(hash_val)
                #print(self.table[hash_val])
                if hash_val == (len(self.table) - 1):
                    hash_val = -1 #to reset index to 0 after end has been reached
                hash_val = hash_val + 1
                #print(hash_val)

            self.table[hash_val] = (key, val)
            self.num_of_keys += 1

        #print(self.table)

        if (self.num_of_keys/len(self.table)) > TOO_FULL:
            self.rehash_after_full()


                
    def hashing_function(self, key):
        hash_val = 0
        for letter in key:
            hash_val = (hash_val*37) + ord(letter)
        hash_val = hash_val % len(self.table)
        return hash_val

    def rehash_after_full(self):
        #print("to rehash", self.table)
        table_to_rehash = self.table[:]    
        self.table = [(None, None)] * len(self.table) * GROWTH_RATIO
        self.num_of_keys = 0 
        for key, val in table_to_rehash:
            if key is not None:
                self.update(key, val)


z = Hash_Table(4, 0)
z.update("d", "hel")
z.update('datboi', 'hello')
z.update("s", "t")
z.update("yo waddup", "zzz")
z.update("sss", "aaa")
z.update("zzz", "ddd")



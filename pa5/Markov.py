# CS122 W'17: Markov models and hash tables
# YOUR NAME HERE

import sys
import math
import Hash_Table

HASH_CELLS = 57

class Markov:

    def __init__(self,k,s):
        '''
        Construct a new k-order Markov model using the statistics of string "s"
        '''
        ### YOUR CODE HERE ###
        #self.k = k
        #self.s = s
        self.gram_counts = self.get_gram_count_table(s, k)




    def log_probability(self,s):
        '''
        Get the log probability of string "s", given the statistics of
        character sequences modeled by this particular Markov model
        This probability is *not* normalized by the length of the string.
        '''
        for character in s:
            k_gram = s[-k+i:] + s[:i]
            kplus_gram = s[-k+i:] + s[:i+1]

            k_count = self.gram_counts.lookup()



def get_gram_count_table(s, k):

    gram_count_table = Hash_Table.Hash_Table(HASH_CELLS, 0)
    for i, character in enumerate(s):
        if i < k:
            k_gram = s[-k+i:] + s[:i]
            kplus_gram = s[-k+i:] + s[:i+1]
        else:
            k_gram = s[i-k:i]
            kplus_gram = s[i-k:i+1]

        #print(k_gram)
        #print(kplus_gram)
    
        k_gram_count = gram_count_table.lookup(k_gram)

        #if k_gram_count == gram_count_table.defval:
        #    gram_count_table.update(k_gram, 1)
        #else:
        gram_count_table.update(k_gram, k_gram_count+1)

        kplus_gram_count = gram_count_table.lookup(kplus_gram)

        #if kplus_gram_count == gram_count_table.defval:
        #   gram_count_table.update(kplus_gram, 1)
        #else:
        gram_count_table.update(kplus_gram, kplus_gram_count+1)

    return gram_count_table


s= "As a result of securing ourselves and ridding the Taliban out of Afghanistan, the Afghan people"
#s = "the three trees there"
k=2





def identify_speaker(speech1, speech2, speech3, order):
    '''
    Given sample text from two speakers, and text from an unidentified speaker,
    return a tuple with the *normalized* log probabilities of each of the speakers
    uttering that text under a "order" order character-based Markov model,
    and a conclusion of which speaker uttered the unidentified text
    based on the two probabilities.
    '''
    ### YOUR CODE HERE ###


def print_results(res_tuple):
    '''
    Given a tuple from identify_speaker, print formatted results to the screen
    '''
    (likelihood1, likelihood2, conclusion) = res_tuple
    
    print("Speaker A: " + str(likelihood1))
    print("Speaker B: " + str(likelihood2))

    print("")

    print("Conclusion: Speaker " + conclusion + " is most likely")

"""

if __name__=="__main__":
    num_args = len(sys.argv)

    if num_args != 5:
        print("usage: python3 " + sys.argv[0] + " <file name for speaker A> " +
              "<file name for speaker B>\n  <file name of text to identify> " +
              "<order>")
        sys.exit(0)
    
    with open(sys.argv[1], "rU") as file1:
        speech1 = file1.read()

    with open(sys.argv[2], "rU") as file2:
        speech2 = file2.read()

    with open(sys.argv[3], "rU") as file3:
        speech3 = file3.read()

    res_tuple = identify_speaker(speech1, speech2, speech3, int(sys.argv[4]))

    print_results(res_tuple)

"""
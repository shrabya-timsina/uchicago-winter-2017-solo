# CS122: Course Search Engine Part 1
#
# Your name(s)
#

import re
import util
import bs4
import queue
import json
import sys
import csv

INDEX_IGNORE = set(['a',  'also',  'an',  'and',  'are', 'as',  'at',  'be',
                    'but',  'by',  'course',  'for',  'from',  'how', 'i',
                    'ii',  'iii',  'in',  'include',  'is',  'not',  'of',
                    'on',  'or',  's',  'sequence',  'so',  'social',  'students',
                    'such',  'that',  'the',  'their',  'this',  'through',  'to',
                    'topics',  'units', 'we', 'were', 'which', 'will', 'with', 'yet'])


### YOUR FUNCTIONS HERE


'''
Function 1) Queue_url(starting_url)
This function will return a queue of websites to visit.
No duplicates.

Function 2) Scrape(html_block)
Given the course_block portion of an html file
Outputs a dictionary/csv with each word of the description as a key, 
and the course code as the value

Function 3) Strip(url)
reduce the soup to blocks of texts of classes 

'''

### YOUR FUNCTIONS HERE





def convert_to_soup(url):

    request = util.get_request(url)
    assert request != None
    html = util.read_request(request)
    assert html != None
    soup = bs4.BeautifulSoup(html, 'lxml')
    return soup

def build_dict(url):
    soup = convert_to_soup(url)
    course_list = soup.find_all('div', class_='courseblock main')
    index_dictionary  = {}
    course_code_map = open_json_key()

    for course_block in course_list:
        
        course_block_title = course_block.find('p', class_='courseblocktitle')
        course_description = course_block.find('p', class_='courseblockdesc')

        sequence = util.find_sequence(course_block)

        #if there are no subsequences
        if not sequence:
            #children = course_block.contents
            #course_code_and_title = children[1].text

            course_code = get_course_code(course_block_title.text)
            course_identifier = course_code_map[course_code]

            words_in_title = get_words_from_title(course_block_title.text)
            words_in_description = get_words_from_description(course_description.text)
            
            all_words = list(set(words_in_title + words_in_description))
            words_to_index = [word for word in all_words if word not in INDEX_IGNORE]    
            index_dictionary[course_identifier] = words_to_index

        else:
            #seq_codes_and_title = course_block.find('p', class_='courseblocktitle')
            
            #course_seq_codes = get_course_code(course_block_title.text)
            #course_code_list = course_seq_codes.split()
            #course_code_list_proper = [course_code_list[0] + ' ' + code for code in course_code_list[1:]]
            
            words_in_seq_title = get_words_from_title(course_block_title.text)
            words_in_seq_description = get_words_from_description(course_description.text)


            for subsequence in sequence:
                
                subsequence_title = subsequence.find('p', class_='courseblocktitle')
                subsequence_description = subsequence.find('p', class_='courseblockdesc')
                
                subsequence_code = get_course_code(subsequence_title.text)
                print(subsequence_code)
                subsequence_identifier = course_code_map[subsequence_code]

                words_in_subseq_title = get_words_from_title(subsequence_title.text)
                
                if subsequence_description is not None:
                    words_in_subseq_description = get_words_from_description(subsequence_description.text)
                else:
                    words_in_subseq_description = []

                all_words = list(set(words_in_seq_title + words_in_seq_description + words_in_subseq_title + words_in_subseq_description))
                words_to_index = [word for word in all_words if word not in INDEX_IGNORE]    
                index_dictionary[subsequence_identifier] = words_to_index    



                


            



    return index_dictionary

def get_course_code(course_code_and_title):
    #get course identifier from course code
    #course_code_pattern = r'[A-Z]{4}\s[0-9]+'
    
    #course_code = re.search(course_code_pattern, course_code_and_title).group()
    #course_code = re.sub('[^A-Za-z0-9]+', ' ', course_code) #remove special character
    #

    course_code = re.match('.+[0-9]+\.', course_code_and_title).group()
    course_code = re.sub('[^A-Za-z0-9/s]+', ' ', course_code)
    course_code = course_code[:-1] #remove space at end

    return course_code     


def get_words_from_title(course_code_and_title):
    #extract words from title
    course_title = course_code_and_title.lower()
    course_title = re.sub('[^A-Za-z0-9]+', ' ', course_title)
    words_pattern = r'[A-Za-z][A-Za-z0-9*]+'
    words_in_title = re.findall(words_pattern, course_title)
    words_in_title = words_in_title[1:] #removing first word which is part of course code
    
    return words_in_title

def get_words_from_description(description):
    words_pattern = r'[A-Za-z][A-Za-z0-9*]+'
    description = description.lower()
    description = re.sub('[^A-Za-z0-9]+', ' ', description) 
    words_in_description = re.findall(words_pattern, description)

    return words_in_description


def open_json_key():
    with open('course_map.json') as json_data:
        course_number_data = json.load(json_data)
    return course_number_data












def go(num_pages_to_crawl, course_map_filename, index_filename):
    '''
    Crawl the college catalog and generates a CSV file with an index.

    Inputs:
        num_pages_to_crawl: the number of pages to process during the crawl
        course_map_filename: the name of a JSON file that contains the mapping
          course codes to course identifiers
        index_filename: the name for the CSV of the index.

    Outputs: 
        CSV file of the index index.
    '''

    starting_url = "http://www.classes.cs.uchicago.edu/archive/2015/winter/12200-1/new.collegecatalog.uchicago.edu/index.html"
    limiting_domain = "cs.uchicago.edu"

    # YOUR CODE HERE


if __name__ == "__main__":
    usage = "python3 crawl.py <number of pages to crawl>"
    args_len = len(sys.argv)
    course_map_filename = "course_map.json"
    index_filename = "catalog_index.csv"
    if args_len == 1:
        num_pages_to_crawl = 1000
    elif args_len == 2:
        try:
            num_pages_to_crawl = int(sys.argv[1])
        except ValueError:
            print(usage)
            sys.exit(0)
    else:
        print(usage)    
        sys.exit(0)


    go(num_pages_to_crawl, course_map_filename, index_filename)





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

def build_dict(url, course_map_filename = 'course_map.json'):
    soup = convert_to_soup(url)
    course_list = soup.find_all('div', class_='courseblock main')
    index_dictionary  = {}
    course_code_map = open_json_key(course_map_filename)

    for course_block in course_list:
        
        course_block_title = course_block.find('p', class_='courseblocktitle')
        course_description = course_block.find('p', class_='courseblockdesc')

        words_in_title = get_words_from_title(course_block_title.text)
        if course_description is None:
            words_in_description = []
        else:
            words_in_description = get_words_from_text(course_description.text)

        sequence = util.find_sequence(course_block)

        if not sequence:

            course_identifier = get_course_identifier(course_block_title.text, course_code_map)          
            
            all_words = set(words_in_title + words_in_description)
            words_to_index = all_words - INDEX_IGNORE
            index_dictionary[course_identifier] = list(words_to_index)

        else:
            
            for subsequence in sequence:
                
                subsequence_title = subsequence.find('p', class_='courseblocktitle')
                subsequence_description = subsequence.find('p', class_='courseblockdesc')
                              
                subsequence_identifier = get_course_identifier(subsequence_title.text, course_code_map)

                words_in_subseq_title = get_words_from_title(subsequence_title.text)
                if subsequence_description is None:
                    words_in_subseq_description = []
                else:
                    words_in_subseq_description = get_words_from_text(subsequence_description.text)
                    
                all_words = set(words_in_title + words_in_description 
                                    + words_in_subseq_title + words_in_subseq_description)
                words_to_index = all_words - INDEX_IGNORE
                index_dictionary[subsequence_identifier] = list(words_to_index)

    return index_dictionary

def get_course_identifier(course_code_and_title, course_code_map):
    course_code = re.match('.+[0-9]+\.', course_code_and_title).group()
    course_code = re.sub('[^A-Za-z0-9/s]+', ' ', course_code)
    course_code = course_code[:-1] #remove space at end
    course_identifier = course_code_map[course_code]
    return course_identifier


def get_words_from_text(text_block):
    text_block = text_block.lower()
    text_block = re.sub('[^a-z0-9]+', ' ', text_block) 
    words_pattern = r'[a-z][a-z0-9]*'
    words = re.findall(words_pattern, text_block)
    return words

def get_words_from_title(course_code_and_title):
    words_in_title = get_words_from_text(course_code_and_title)
    words_in_title = words_in_title[1:] #removing first word which is part of course code
    return words_in_title

def open_json_key(course_map_filename):
    with open(course_map_filename) as json_data:
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





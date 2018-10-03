#!/usr/bin/env python

###################################################
### IMPORT UTILITIES ##############################
###################################################

# Thanks to Marco's great writeup: https://marcobonzanini.com/2015/02/25/fuzzy-string-matching-in-python/

### FuzzyWuzzy String Matching Algorithms ###
# pip install fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

### Levenshtein String Matching Substitution Algorithms ###
# pip install python-Levenshtein
import Levenshtein as lev

###################################################
### FUNCTIONS #####################################
###################################################

def str_fuzzy_score_full(str1, str2):
    """
    - Description -
    ---------------
    Return score (0-100) on how similar two strings are.
        
        - Takes full words, punctuation, and spaces into account.
        - Use str_fuzzy_partialscore() instead to test if string in other string.
    
    - Parameters -
    ---------------
    str1,str2 : two strings
    
    - Returns - 
    ---------------
    similarity score : int
    
    """
    return fuzz.ratio(str1,str2)

def str_fuzzy_score_partial(str1, str2):
    """
    - Description -
    ---------------
    Return score (0-100) on if one string can be found in the other string.
    
    - Parameters -
    ---------------
    str1,str2 : two strings
    
    - Returns - 
    ---------------
    similarity score : int
    
    """
    return fuzz.partial_ratio(str1,str2)

def str_fuzzy_score_sort(str1, str2):
    """
    - Description -
    ---------------
    Return score (0-100) on whether all words in one string all appear in the other string.
        
        - Breaks words apart by white spaces.
        - Removes all punctuation (keeps numbers).
        - Lowercases all letters.
        - Sorts the words, and then checks matches.
    
    - Parameters -
    ---------------
    str1,str2 : two strings
    
    - Returns - 
    ---------------
    similarity score : int
    
    """
    return fuzz.token_sort_ratio(str1,str2)

def str_fuzzy_score_set(str1, str2):
    """
    - Description -
    ---------------
    Return score (0-100) on whether set of words in one string are a subset of the other string.
        
        - Breaks words apart by white spaces.
        - Removes all punctuation (keeps numbers).
        - Lowercases all letters.
        - Sorts the words, and then checks matches.
        - Words must be equal, 
    
    - Parameters -
    ---------------
    str1,str2 : two strings
    
    - Returns - 
    ---------------
    similarity score : int
    
    """
    return fuzz.token_set_ratio(str1,str2)

def str_fuzzy_match_full(str_in, list_in, limit=5): 
    """
    - Description -
    ---------------
    Return best matches from a list to a query string.
        - Takes full words, punctuation, and spaces into account.
        - Use str_fuzzy_partialscore() instead to test if string in other string.
    
    - Parameters -
    ---------------
    str_in : query string
    list_in : list of strings to match against
    limit : number of matches to return
    
    - Returns - 
    ---------------
    similarity score : int
    
    """
    return process.extract(str_in, list_in, scorer=fuzz.ratio, limit=limit)

def str_fuzzy_match_partial(str_in, list_in, limit=5): 
    """
    - Description -
    ---------------
    Return best matches from a list to a query string if one string can be found in the other string.
        - Takes full words, punctuation, and spaces into account.
        - Removes prefix and suffix.
    
    - Parameters -
    ---------------
    str_in : query string
    list_in : list of strings to match against
    limit : number of matches to return
    
    - Returns - 
    ---------------
    similarity score : int
    
    """
    return process.extract(str_in, list_in, scorer=fuzz.partial_ratio, limit=limit)

def str_fuzzy_match_sort(str_in, list_in, limit=5): 
    """
    - Description -
    ---------------
    Return best matches from a list to a query string based on words.
        - Breaks words apart by white spaces.
        - Removes all punctuation (keeps numbers).
        - Lowercases all letters.
        - Sorts the words, and then checks matches.
    
    - Parameters -
    ---------------
    str_in : query string
    list_in : list of strings to match against
    limit : number of matches to return
    
    - Returns - 
    ---------------
    similarity score : int
    
    """
    return process.extract(str_in, list_in, scorer=fuzz.token_sort_ratio, limit=limit)

def str_fuzzy_match_set(str_in, list_in, limit=5): 
    """
    - Description -
    ---------------
    Return best matches from a list to a query string based on words in a set.
        - Breaks words apart by white spaces.
        - Removes all punctuation (keeps numbers).
        - Lowercases all letters.
        - Sorts the words, and then checks matches.
    
    - Parameters -
    ---------------
    str_in : query string
    list_in : list of strings to match against
    limit : number of matches to return
    
    - Returns - 
    ---------------
    similarity score : int
    
    """
    return process.extract(str_in, list_in, scorer=fuzz.token_set_ratio, limit=limit)
    
    
#str_fuzzy_match_full('a dog and cat', ['cats and dogs','a cat and dog','dog and cat','cat and dog are running'], limit=4)
#str_fuzzy_match_partial('a dog and cat', ['cats and dogs','a cat and dog','dog and cat','cat and dog are running'], limit=4)
#str_fuzzy_match_sort('a dog and cat', ['cats and dogs','a cat and dog','dog and cat','cat and dog are running'], limit=4)
#str_fuzzy_match_set('a dog and cat', ['cats and dogs','a cat and dog','dog and cat','cat and dog are running'], limit=4)




#######################################
from collections import Counter   
def count_words_fast(text):
    """
    Counts the number of times each word appear in text(str). Returns dictionary 
    of being key is word in text and value is counts of words. Skip punctuation
    """
    text = text.lower()
    skip = [".", ":", ";", "?", ",", "'", '"']
    for sk in skip:
        text = text.replace(sk, "")
    word_counts = Counter(text.split(" "))
    return word_counts

    
#####################
def read_book(title_path):
    """
    read the book and return as string
    """
    with open(title_path, "r", encoding = "utf8") as current_path:
        text = current_path.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

#####################
def word_stats(word_counts):
    """ 
    Return number of length of word and frequencies of word.
    """
    num_unique = len(word_counts)
    count = word_counts.values()
    return (num_unique, count)

#########################
"""
   After running below code you can access stats DataFrame and see the statistics
   for book just we have read.
   Access stats Dataframe by simply typing stats or stats.head() to look at first
   five row of DataFrame.
"""
import os
book_dir = "./Books"

import pandas as pd
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words_fast(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt",""), sum(counts), num_unique
            title_num += 1


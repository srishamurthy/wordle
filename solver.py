import numpy as np
import math

import os
import json

Data_Dir = os.path.dirname(os.path.realpath(__file__))

Short_Word_File = os.path.join(Data_Dir, "possible_words.txt")
Long_Word_File = os.path.join(Data_Dir, "allowed_words.txt")

Word_Freq_File = os.path.join(Data_Dir, "wordle_words_freq.txt")
Word_Freq_Map_File = os.path.join(Data_Dir, "freq_map.json")

# read datasets

def get_words(short = False):
    word_list = []
    assert os.path.exists(Short_Word_File) and os.path.exists(Long_Word_File)
    file = Short_Word_File if short else Long_Word_File
    with open(file) as fp:
        word_list.extend(word.strip() for word in fp.readlines())
    return word_list

def get_word_freq(regenerate_map = False):
    if os.path.exists(Word_Freq_Map_File) and not regenerate_map:
        with open(Word_Freq_Map_File) as fp:
            word_freq_map = json.load(fp)
        return word_freq_map
    
    # regenerate word frequency map
    word_freq_map = dict()
    assert os.path.exists(Word_Freq_File)
    with open(Word_Freq_File) as fp:
        #TBD

# apply sigmoid fct

# generate color patterns for words

# entropy computations
# I = -log2(p)
# E[I] = sum_x p(x) * I(x)
# E[I] = sum_x p(x) * log2(1/p(x))

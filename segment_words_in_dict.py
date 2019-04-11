# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:46:54 2019

@author: gaurav
"""


def words_in_dict(diction, word):
    """check if we can break this
    word into smaller words that
    exist in the dictionary"""
    if not word:
        return []
    if word in diction:
        return [word]

    #  for i in range(1, len(word)):  # shortest first
    for i in range(len(word), 0, -1):  # longest first
        if word[0:i] in diction:
            inner = words_in_dict(diction, word[i:])
            if inner:
                return [word[0:i]] + inner
    return None


dic = ('a', 'aa', 'aaa', 'aaaa', 'b', 'bab')
print(words_in_dict(dic, 'aaaaaaaaab'))
print(words_in_dict(dic, 'aaaaaaaabab'))
print(words_in_dict(dic, 'aac'))

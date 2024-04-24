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


def segment_words(diction, word):
    """
    using dynamic programming checks
    if a word starts from a location
    """
    memo = []
    for i in range(len(word)):
        memo.append([])
        for j in range(len(diction)):
            memo[i].append(0)

    for i in range(len(word)):
        for j in range(len(diction)):
            dword = diction[j]
            if len(word[i:]) >= len(dword):
                memo[i][j] = int(word[i:i+len(dword)] == dword)

    [print(_) for _ in memo]



dic = ['a', 'aa', 'aaa', 'aaaa', 'b', 'bab']
print(words_in_dict(dic, 'aaaaaaaaab'), segment_words(dic, 'aaaaaaaaab'))
print(words_in_dict(dic, 'aaaaaaaabab'), segment_words(dic, 'aaaaaaaabab'))
print(words_in_dict(dic, 'aac'), segment_words(dic, 'aac'))

dic = ["i", "like", "sam", "sung", "samsung", "mobile", "man", "mango"]
print(words_in_dict(dic, 'ilikesamsung'), segment_words(dic, 'ilikesamsung'))
print(words_in_dict(dic, 'ilikesamgo'), segment_words(dic, 'ilikesamgo'))
print(words_in_dict(dic, 'ilikesaman'), segment_words(dic, 'ilikesaman'))

dic = ["pine", "apple", "pen"]
print(words_in_dict(dic, 'applepineapple'), segment_words(dic, 'applepineapple'))

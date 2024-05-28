# -*- coding: utf-8 -*-
"""
Created on Tue May 28 03:33:28 2024

@author: gaurav
"""
def can_split_str_by_dictionary(s, dict: set):
    """Given a string and dictionary of words,
    break the string in valid list of words"""
    if not s:
        return True
    if not dict:
        return False
    for word in dict:
        if len(s) < len(word):
            continue
        if s[:len(word)] == word:
            # Can't repeat words from dict
            dict.remove(word)
            res = can_split_str_by_dictionary(s[len(word):], dict)
            if res:  # able to split
                return True
            # Could not split, retry
            dict.add(word)
    return False


FN = can_split_str_by_dictionary
print("====", FN.__name__)
print(FN("leetcode", {"lee", "eet", "leet", "code"}))
print(FN("catsanddog", {"cat", "cats", "and", "sand", "dog"}))
print(FN("catsandog", {"cats", "dog", "sand", "and", "cat"}))
print(FN("abcd", {"a", "abc", "b", "cd"}))
print(FN("aaaa", {"a", "aa", "aaa"}))
print(FN("aaaa", {"a", "aa", "aaaaaa"}))
print(FN("pineapplepenapple", {"apple", "pen", "applepen", "pine", "pineapple"}))


def split_str_by_dictionary(s, dict: set):
    """Actually split string by words"""
    if not s: return ''
    if not dict: return None

    for word in dict:
        if len(s) < len(word):
            continue
        if s[:len(word)] == word:
            # Can't repeat words from dict
            dict.remove(word)
            res = split_str_by_dictionary(s[len(word):], dict)
            if res is not None:  # able to split
                return f"{word} {res}"
            # Could not split, retry
            dict.add(word)
    return None


FN = split_str_by_dictionary
print("====", FN.__name__)
print(FN("leetcode", {"lee", "eet", "leet", "code"}))
print(FN("catsanddogs", {"cat", "cats", "and", "sand", "dogs"}))
print(FN("catsandogs", {"cats", "dogs", "sand", "and", "cat"}))
print(FN("abcd", {"a", "abc", "b", "cd"}))
print(FN("aaaa", {"a", "aa", "aaa"}))
print(FN("aaaa", {"a", "aa", "aaaaaa"}))
print(FN("pineapplepenapple", {"apple", "pen", "applepen", "pine", "pineapple"}))

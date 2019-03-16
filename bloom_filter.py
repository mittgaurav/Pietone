# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 03:14:47 2019

@author: gaurav

BloomFilter probabilistic data structure
says whether an element is already seen/
present in data. It runs multiple hashes
on element and set bits corresponding to
those hashes. And to check existence, it
reverses the process. Now, if those same
bits are set by multiple other elements,
we may have a false positive. Though, it
guarantees no false negatives. i.e. when
it says an element isn't there, it isn't

Hash function can be improved vastly.
"""
import random
from bitarray import bitarray


class BloomFilter():
    """n-len set and k hash fns
    to check whether an element
    is either definitely not in
    there or possibly is there"""
    def __init__(self, m_bits, k_hashes):
        self.m = m_bits
        self.k = k_hashes
        self.bits = bitarray(m_bits)
        self.bits.setall(0)

    def hasher(self, num):
        """hash iterator"""
        for i in range(self.k):
            yield (num + i) % self.m

    def add(self, num):
        """add num to filter"""
        for i in self.hasher(num):
            self.bits[i] = 1

    def __contains__(self, num):
        for i in self.hasher(num):
            if self.bits[i] == 0:
                return False
        return True


if __name__ is "__main__":
    N = 10000
    BF = BloomFilter(N, 100)
    Ns = list()
    for _ in range(100):
        n = int(random.random() * 10000)
        BF.add(n)
        Ns.append(n)

    # definitely no false negative
    # if element not there, say so
    assert not [print("error with", i) for i in Ns if i not in BF]

    # false positives are possible
    total = 0
    for _ in range(N):
        n = int(random.random() * 10000)
        if n not in Ns and n in BF:
            total += 1
            # print(total, "warning", n)

    print("perfection", 100 - (total/N * 100), "percent")

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:05:37 2020

leetcode.com/discuss/interview-question/538068/

@author: gaurav
"""


def get_tuple(N, this):
    """given row digits and col char
    returns the unique tuple number"""
    row, col = get_row_col(this)
    return get_tuple_2(N, row, col)


def get_row_col(this):
    """return tuple of row and col
    from '12A', '1A', etc. strs"""
    return int(this[:-1]), ord(this[-1]) - ord('A')


def get_tuple_2(N, row, col):
    """for everything figured out"""
    return (N * (row - 1)) + col


def solution(N, S, T):
    """given battleship locations and
    hits, get number of ships totally
    sunk and only hit but not sunk"""
    # determine ships
    ships = S.split(',')

    # determine hits - for each ship how many hit
    hits = T.split(' ')
    hits = set([get_tuple(N, h) for h in hits])

    ships_sunk = 0
    ships_hit = 0
    for ship in ships:
        # for each ship, figure out ends
        this = ship.split(' ')

        left_row, left_col = get_row_col(this[0])
        right_row, right_col = get_row_col(this[1])

        # determine all tuples for this ship
        ship_locs = []
        for row in range(left_row, right_row + 1):
            for col in range(left_col, right_col + 1):
                ship_locs.append(get_tuple_2(N, row, col))

        # Now, determine if all
        # locations in this hit
        ship_locs = set(ship_locs)
        ship_hits = ship_locs.intersection(hits)
        if len(ship_hits) == len(ship_locs):
            ships_sunk += 1
        elif len(ship_hits) > 0:
            ships_hit += 1

    return f'{ships_sunk},{ships_hit}'


print(solution(4, '1B 2C,2D 4D', '2B 2D 3D 4D 4A') == '1,1')
print(solution(3, '1A 1B,2C 2C', '1B') == '0,1')
print(solution(12, '1A 2A,12A 12A', '12A') == '1,0')

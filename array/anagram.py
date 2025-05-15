from collections import Counter, defaultdict


def hashed(s):
    count = Counter(s)
    h = []
    for c in "abcdefghijklmnopqrstuvwxyz":
        h.append(str(count[c]))
    return "$".join(h)


def group_anagrams(words):
    if not words:
        return words

    if len(words) == 1:
        return [words]

    result = defaultdict(list)
    for s in words:
        result[hashed(s)].append(s)

    return result.values()


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    str2 = 'th'
    n1 = len(word)
    n2 = len(str2)

    # Base Case
    if (n1 == 0 or n1 < n2):
        return 0

    if (word[0: n2] == str2):
        return 1 + count_th(word[n2 - 1:])

    return count_th(word[n2 - 1:])

'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    try:
        th_index = word.index('th')
        return 1 + count_th(word[th_index+2:])
    except:
        return 0

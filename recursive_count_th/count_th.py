'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    word_looking_for = "th"
    if len(word) < 2:
        return "Length of word cannot be less than 2"
    if word[:2] == word_looking_for:
    ## if word[ from index0 - 2] contains "th"
        return count_th(word[1:]) +1
        ## return the word[ starting at the 1st index] + 1
        ## showing the word was found
    else:
        return count_th(word[1:])
                ## return the word[ starting at the 1st index] + 1

w_1 = "abcthxyz"   #1 occurences
w_2 = "abcthefthghith" # 3 occurences
w_3 = "thhtthht" #2 occurences

print(count_th(w_1))
print(count_th(w_2))
print(count_th(w_3))
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

#! used  logical operators  to accomplish. tests pass
def count_th(word, count = 0):
    count = 0
    word_looking_for = "th"
    th_length = 2
    if len(word) < th_length:
        return 0
    if word[0] == word_looking_for[0] and word[1] == word_looking_for[1]:
        count += 1
    ## if word[ from index0 - 2] contains "th"
        return count + count_th(word[1:])
        ## return the word[ starting at the 1st index] shaving off the 0 index
        ##  + 1  showing the word was found
    else:
        return count_th(word[1:])
                ## return the word[ starting at the 1st index] with no update to return value
                ## because th was not found
w_1 = "abcthxyz"   #1 occurences
w_2 = "abcthefthghith" # 3 occurences
w_3 = "thhtthht" #2 occurences
w_4 = "t" #0 occurences
w_5 = "th" # 1

print(count_th(w_1))
print(count_th(w_2))
print(count_th(w_3))
print(count_th(w_4))
print(count_th(w_5))
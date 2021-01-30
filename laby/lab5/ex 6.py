# Ex. 6. Write a function that removes duplicdef remove_dup(s):
def remove_dup(s):
    mylist = list(s)
    mylist = list( dict.fromkeys(mylist) )
    mylist="".join(mylist)
    return mylist


if remove_dup('aaaaa') == 'a' and remove_dup('abababab') == 'ab' and remove_dup('abcbasdbrwefj') == 'abcsdrwefj':
    print('Correct')
else:
    print('Incorrect')


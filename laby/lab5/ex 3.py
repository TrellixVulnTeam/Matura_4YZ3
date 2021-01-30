#Ex. 3. Write a function that removes each occurrence of a given letter from a string. (Of course strings are immutable, so return new string without this letter.)
def rm_let_from_str(letter, string):
    li=[]
    for x in string:
        if (x==letter):
            continue
        else:
            li.append(x)
    new_string="".join(li)
    return new_string

if rm_let_from_str('a', 'apple') == 'pple' and rm_let_from_str('s', 'somestringwithmoreletters') == 'ometringwithmoreletter' and rm_let_from_str('a', 'aaaaaa') == '':
    print('Correct')
else:
    print('Incorrect')
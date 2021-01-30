#Ex 4. Write function that recognizes whether something is a palindrome.
def is_palindrome(s):
    la=list(s)
    lb=list(s)
    lb.reverse()
    for x in range(len(la)):
        if la[x]==lb[x]:
            continue
        else:
            return False
    return True

if is_palindrome('aaaaa') and is_palindrome('ababa') and not is_palindrome('aaabbb'):
    print('Correct')
else:
    print('Incorrect')
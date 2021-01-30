#Ex. 2. Write a function that returns a number of digits of an integer.
def count_digits(n):
    n=str(n)
    return len(n)

if count_digits(123) == 3 and count_digits(1) == 1 and count_digits(12342938473) == 11:
    print('Correct')
else:
    print('Incorrect')
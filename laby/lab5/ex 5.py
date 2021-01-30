def count_occ(string, substring):
    return string.count(substring)


if count_occ('banana', 'na') == 2 and count_occ('aaaaaaaa', 'aa') == 4 and count_occ('banana', 'h') == 0:
    print('Correct')
else:
    print('Incorrect')
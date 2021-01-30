l = ['ahj', 'bfdf', 'c', 'd', 'a', 'g', 'a', 'h', 'b', 'a', 'aaa', 'razdwatrzy']
a = 'razdwatrzy'


def count(li, x):
    '''
    Return the number of times x appears in the list.
    '''
    ans = 0
    for i in range(len(li)):
        if li[i] == x:
            ans += 1
    return ans


print(count(l, a))


# There is no in function, implement keyword in
def is_in(li, x):
    '''
    Returns True if x is in list and False otherwise
    '''
    for i in range(len(li)):
        if li[i] == x:
            return True
        else:
            continue
    return False


print(is_in(li, a))


def index(li, x):
    '''
    Return zero-based index in the list of the first item whose value is equal to x.
    Return -1 if there is no such item.
    '''
    for i in range(len(li)):
        if li[i] == x:
            return i
    return -1


print(index(li, a))


def insert(li, x, pos):
    l1 = []
    for i in range(pos):
        l1.append(l[i])
    l1.append(x)
    for i in range(pos + 1, len(l)):
        l1.append(l[i])
    '''
    Insert an item at a given position.
    '''

    return print(l1)


print(insert(li, a, 5))
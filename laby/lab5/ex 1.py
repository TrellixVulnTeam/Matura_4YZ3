l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=int(input())
print(l[0:n])
print(l[len(l)-n:])
print(l[n:len(l)])
print(l[:len(l)-n])
print(l[::n])
print(l[::-1])

"""
Ex. 1. Use slicing notation to get:

first n items
last n items
all but first n items
all but last n items
every nth element (from beggining)
reverse the list

"""
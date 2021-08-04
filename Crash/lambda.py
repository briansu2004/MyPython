a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]

# in filter either we use assignment or
# conditional operator, the pass actual
# parameter will get return
filtered = filter(lambda x: x % 2 == 0, a)
print(list(filtered))

# in map either we use assignment or
# conditional operator, the result of
# the value will get returned
maped = map(lambda x: x % 2 == 0, a)
print(list(maped))

from collections import defaultdict

##############################################################
Dict = {1: 'Looking', 2: 'For', 3: 'Scala', 4: "roles"}
print("Dictionary:")
print(Dict)
print(Dict[1])

##############################################################


def def_value():
    return "Can't find it"


# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])

##############################################################
d = defaultdict(lambda: "Not exists")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])


##############################################################
d = defaultdict(lambda: "This key is not found")
d["a"] = 1
d["b"] = 2

# Provides the default value
# for the key
print(d.__missing__('a'))
print(d.__missing__('d'))


##############################################################
# Defining a dict
d = defaultdict(list)

for i in range(5):
    d[i].append(i * i)

print("Dictionary with values as list:")
print(d)

##############################################################
# Defining the dict
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list
# for keeping the count
for i in L:

    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1

print(d)

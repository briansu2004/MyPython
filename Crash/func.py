
def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2


def myFun(x):
    x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)


def myFun1(x):
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]


# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun1(lst)
print(lst)


def myFun2(x):

    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20


# Driver Code (Note that lst is not modified
# after function call.
x = 10
myFun2(x)
print(x)

print(square_value.__doc__)

print(square_value(2))

print(square_value(-4))

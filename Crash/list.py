def odd_sqaure(num):
    odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
    print(odd_square)
    even_cube = [x ** 3 for x in range(1, num) if x % 2 == 0]
    print(even_cube)


if __name__ == "__main__":
    odd_sqaure(10)

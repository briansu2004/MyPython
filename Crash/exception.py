def throw_exception(num):
    if num == 0:
        raise Exception("Arg can't be 0")
    else:
        print(num)


def trycatch(num):
    try:
        throw_exception(num)
    except Exception as ex:
        print(ex)
    else:
        print("All good")
    finally:
        print("Done")


trycatch(0)

trycatch(1)

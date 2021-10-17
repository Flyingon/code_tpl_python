import copy


class ABC:
    number = 1
    string = "2"


if __name__ == '__main__':
    a = ABC()
    b = copy.deepcopy(a)
    b.string = "3"
    print(a.string, b.string)
    print()

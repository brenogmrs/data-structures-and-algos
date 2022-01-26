# constante -> O(1)
my_list = [1, 2, 3, 4, 5]


def constant(my_list):
    print(my_list[0])


# Linear -> O(n)


def linear(my_list):
    for i in my_list:
        print(i)


# Quadratic -> O(n^2)


def quadratic(my_list):
    for i in my_list:
        for j in my_list:
            print(i, j)
        print("-------")


# Combination


def combination(my_list):
    print(my_list[0])

    for i in range(5):
        print("test, ", i)

    for i in my_list:
        print(i)

    for i in my_list:
        print(i)

    print("----python----")

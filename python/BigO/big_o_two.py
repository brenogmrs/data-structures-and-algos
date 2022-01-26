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

# O(7) + O(2n) -> O(n)
def combination(my_list):
    # O(1)
    print(my_list[0])

    # O(5)
    for i in range(5):
        print("test, ", i)

    # O(n)
    for i in my_list:
        print(i)
    # O(n)
    for i in my_list:
        print(i)

    # O(1)
    print("----python----")

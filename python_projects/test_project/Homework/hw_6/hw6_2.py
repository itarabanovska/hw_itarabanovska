# a = 9
# numbers = []
# for i in range(1, a + 1):
#     if a % i == 0:
#         numbers.append(i)
# print(numbers)


def numbers(a):
    number_list = []
    for i in range(1, a + 1):
        if a % i == 0:
            number_list.append(i)
    return number_list

print(numbers(6))
# a = 'this is a cool phrase'
# w = ''
# words = []
# for i in a:
#     if i != ' ':
#         w += i
#     else:
#         words.append(w)
#         w = ''
# words.append(w)
# print(words)
#
# first_letters = ''
# for i in words:
#     first_letters += i[0].upper()
# print(first_letters)


# a = 'this is a cool phrase'
# acro = ''
# for i in a.split():
#     acro += i[0].upper()
# print(acro)

def acro(a):
    result = ''
    for i in a.split():
        result += i[0].upper()
    return result

print(acro('fgh kjhg'))


def my_filter(lambd, rang):
    a = []
    for i in rang:
        if lambd(i):
            a.append(i)
    return a

res = my_filter(lambda x: x > 0, range(-10, 10))
res2 = list(filter(lambda x: x > 0, range(-10, 10)))

print(res)
print(res2)




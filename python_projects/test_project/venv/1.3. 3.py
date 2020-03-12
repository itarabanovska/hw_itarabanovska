import random
user_accounts = {
    'cat': ['dfdss', 78493487],
    'dog': ['qwesfd', 89638492],
    'rat': ['fgyjgf', 90906545],
    'pig': ['fgrtgh', 81234234],
    'cow': ['gtwxz', 69785948],
    'elephant': ['lkol', 55889087],
    'cammel': ['vfdd', 10293847],
    'tiger': ['gfgeer', 20390004],
    'leon': ['gftynnn', 45678034],
    'zebra': ['grtyt', 20906540],
}


login = input('Please enter your login:')
if login in list(user_accounts.keys()):
    print(user_accounts[login])
else:
    password = (input('Enter your password:'))
    secret = random.randint(1000, 1000000)
    print(user_accounts.setdefault(login, [password, secret]))

print(user_accounts)





import make_password
a = input("How many characters?: ")
if a == '':
    a = 8
a = int(a)
strong = make_password.setup()
strong.writeFile(mode="cute", length=a)







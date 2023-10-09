import make_password
a = input("何文字にしたいですか？デフォルトで8文字: ")
if a == '':
    a = 8
a = int(a)
strong = make_password.setup()
strong.writeFile(mode="cute", length=a)







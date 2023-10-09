# password_assemble
##This program is used to create strong password.

##_How to use_
soft_password.py: This program reproductions "Suggests New Password".
And you can keep a password in "myfile.txt".

cute_password.py: This program conscious to compact.
"Compact" that I said is "use lower characters and one symbol(_)".
You can use this to create new mailadress and user name.

make_password.py: This git's main. And you can create new app from this 
program.
ex.
import make_password
strong = make_password.setting()
strong.writeFile(mode="basic")

-->Would you like use symbol in the password?[y/n]: y
-->Wrote down such as this password: [password shown]

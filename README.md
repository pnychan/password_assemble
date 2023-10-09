#password_assemble --パスワード集#
##This program is used to create strong password.
  --このプログラムは強力なパスワードを作ってくれます。##

_How to use_　使い方<br>
**soft_password.py**: This program reproductions "Suggests Strong Password" usually you used.
And you can keep a password in "myfile.txt".
**soft_password.py**: このプログラムは皆さんおなじみの「強力なパスワードの提案」を
忠実に再現したものです。そして、生成したパスワードは"mifile.txt"に保存することができます。

**cute_password.py**: This program conscious to compact.
"Compact" that I said is "use lower characters and one symbol(_)".
You can use this to create new mailadress and user name.
**cute_password.py**: このプログラムはコンパクトで覚えやすいを意識して作ったものです。
あなたはそこでパスワードの文字数を選ぶことができます。
メールアドレスとユーザー名で迷ったときに使えます。

**make_password.py**: This git's main. And you can create new app from this 
program. There are example↓
**make_password.py**: このgitのメイン部分です。ほとんどのプログラムはこのmake_passwordに頼っています。
つまりこのプログラムによって新しいアプリを作ることができると言い換えることができます。
下に例があります↓
ex. 例）
1.
import make_password
strong = make_password.setting()
strong.writeFile(mode="basic")

-->Use symbol?[y/n]: y
<br>-->Password: [password shown]

2.
import make_password
strong = make_password.setting()
strong.writeFile(dize=strong.randomPass(9, mode="micro"))

-->Password: [password shown]


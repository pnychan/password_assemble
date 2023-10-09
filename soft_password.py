"""Microsoft edgeの強力なパスワード 再現
Microsoftのパスワードの特徴:
1.少なくとも!, _, -, :, .が含まれる
2.パスワードの文字数は全て15文字の可能性が高い"""

import make_password
written = ""
strong = make_password.setup()
strong.writeFile(dize=strong.randomPass(15, mode="micro"))


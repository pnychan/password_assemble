import secrets
import string
import random

written = ""
a = ""
pass_chars = ""
ex_characters = "..__:!"
password = ""

def error(contain, function=None):
    print(function+"()にエラー発生: "+contain)


class setup:
    def symbol_replace(self, strings):
        import re
        global pass_chars
        time = 0
        symbol = 0
        pattern = r'[!_:.]+'
        sentence = strings
        #strings = strings[:1]
        for i in range(len(sentence)):
            try:
                match = re.search(pattern, strings[i])

                if match:
                    if symbol > 0:
                        sentence = sentence.replace(sentence[i], '')
                        time = time + 1
                    symbol = 2
                symbol = symbol - 1
            except:
                break
        pass_chars = string.ascii_letters
        r = self.randomPass(time, mode="basic")
        sentence = sentence + r

        return sentence
    

    def randomPass(self, length, mode="basic"):
        global pass_chars, password
     
        if mode == "basic":
              pass
        elif mode == "micro":
             pass_chars = string.ascii_letters + ex_characters
             password = ''.join(secrets.choice(pass_chars) for x in range(length))
             password = self.symbol_replace(password)
             return password
        elif mode == "cute":
            pass_chars = string.ascii_lowercase + string.digits + '___'
        else:
             error("The mode isn't defined.", function="randomPass")
             return
        password = ''.join(secrets.choice(pass_chars) for x in range(length))
        return password
    
    
    
    def writeFile(self, mode="basic", file="myfile.txt",
                  length=None, dize=True):
        global written
        f = open(file, 'w')
        if length == None:
            r = random.randint(8, 12)
        else:
            r = length
        if dize == True:
            written = self.randomPass(r, mode=mode)
        else:
            written = dize
        f.write(written)

        f.close()
        print("Password: "+written)

    def ask(self):
        global a, pass_chars
        a = input("Use symbol?[y/n]: ")
        if a == "n":    
            pass_chars = string.ascii_letters
        else:
            pass_chars = string.ascii_letters + string.digits+string.punctuation

def main():
    strong = setup()
    strong.ask()
    strong.writeFile()

if __name__ == '__main__':
    main()

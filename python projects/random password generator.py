import random
import string
def password():
    length=int(input("Enter desired password length :"))
    num=int(input("number of numbers in the password :"))
    letter=int(input("number of alphabets in the password :"))
    punc=int(input("number of special numbers in th password :"))
    if num+letter+punc>length:
        print("Desired numbers doesn't match password length. TRY AGAIN !!!")
        return
    else:
        n=random.choices(string.digits,k=num)
        alpha=random.choices(string.ascii_letters,k=letter)
        special=random.choices(string.punctuation,k=punc)

        password_list=n+alpha+special
        random.shuffle(password_list)

        print("------Generated Password-------")
        print(''.join(password_list))


password()
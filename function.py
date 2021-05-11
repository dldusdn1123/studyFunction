def printhello():
    print("Hello, user")

printhello()


def printhi(name):
    print("Hi", name)

name = input("이름을 입력: ")
printhi(name)

def printWelcome(user):
    word = "Welcome, " + str(user)
    return word

user = input("당신의 이름은? ")
print(printWelcome(user))

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

a, b, c =func_mul(10)
print(a,b,c)
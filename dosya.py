import os
if not os.path.exists("./dosya"):
    os.makedirs("dosya")
dosya = open("./dosya/input.txt","w")

a = input("please enter two numbers with space bar: ")


try:
    with open("./dosya/input.txt", "a") as abc:
        abc.writelines(a)
except:
        print("dosyada hata oldu.")


dosya= open("./dosya/output.txt","w")
a = a.split(" ")
length = len(a)
total = 0
for i in range(length):
    if a[i] <= a[length -1]:
     total = total + int(a[i])


try:
    with open("./dosya/output.txt", "a") as abc:
        abc.writelines(str(total))
except ZeroDivisionError :
    print("zero division")
except KeyError :
    print("key error")
except NameError :
    print("name error")
except SyntaxError :
    print("syntax error")
except SystemError :
    print("system error")
except ModuleNotFoundError:
    print("module not found")
except KeyboardInterrupt :
    print("keyboard interrupt")
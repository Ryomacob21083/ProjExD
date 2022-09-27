import random
import datetime

q = 0
a = 0
r = 0

num = random.randint(1, 4)
if num == 1:
    q = "サザエの旦那の名前は？"
elif num == 2:
    q = "カツオの妹の名前は？"
elif num == 3:
    q = "タラオはカツオから見てどんな関係？"

print("問題：")
print(q)
st = datetime.datetime.now()
a = input("答えるんだ：")


if num == 1:
    if a == "マスオ" or a == "ますお":
        r = "正解"
    else:
        r = "出直してこい"
elif num == 2:
    if a == "ワカメ" or a == "わかめ":
        r = "正解"
    else:
        r = "出直してこい"
elif num == 3:
    if a == "甥" or a == "おい" or a == "甥っ子" or a == "おいっこ":
        r = "正解"
    else:
        r = "出直してこい"

ed = datetime.datetime.now()
print(r)
print((ed-st).seconds)
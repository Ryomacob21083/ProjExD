import random
import datetime
from site import abs_paths

num_of_alphabet = 26  # 全アルファベット数
num_of_all_chars = 10 # 対象文字数
num_of_abs_chars = 2  # 欠損文字数
num_of_trials = 2     # チャレンジできる回数
abs_chars = []
judge = 1
count = 0

def shutudai(alphabet):
    global abs_chars
    all_chars = random.sample(alphabet, num_of_all_chars)
    print("対象文字：")
    for i in sorted(all_chars):
        print(i, end=" ")
    print()

    abs_chars = random.sample(all_chars, num_of_abs_chars)
    print("表示文字：")
    for i in all_chars:
        if i not in abs_chars:
            print(i, end=" ") 

def kaitou():
    ans_1 = int(input("欠損文字はいくつあるでしょうか？："))
    if ans_1 == num_of_abs_chars:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください。")
        ans_2 = input("１つ目の文字を入力してください：")
        ans_3 = input("２つ目の文字を入力してください：")

        if (ans_2 in abs_chars) and (ans_3 in abs_chars):
            print("正解です。おめでとうございます。")
            judge = 0
        else:
            print("不正解です。またチャレンジしてください。")
            print("--------------------------------------------")
    else:
        print("不正解です。またチャレンジしてください。")
        print("--------------------------------------------")


if __name__ == "__main__":
    alphabet  =[chr(i+65) for i in range(num_of_alphabet)]
    while judge == 1:
        shutudai(alphabet)
        print("\n")
        kaitou()
        count += 1
        if count == 2:
            break

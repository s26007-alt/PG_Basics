answers = [23, 6, 19, 37, 43]

while True:
    n = input("なにか数字を入れてください->")
    if n == 'q':
        break
    else:
        if int(n) in answers:
            print("正解！")
        else:
            print("数字を入力するか、qで終了します")

import random

y = int(input("ジャンケンポン！(グー:1,チョキ:2,パー:3)"))
c = random.randint(1,3)

if y == 1:
    print("あなたの手:グー")
    if y == 2:
        print("あなたの手:チョキ")
    if y == 3:
        print("あなたの手:パー")

elif c == 1:
    print("コンピューターの手:グー")
    if c == 2:
        print("コンピューターの手:チョキ")
    if c == 3:
        print("コンピューターの手:パー")


if y == 1:
    if c == 1:
        print("あいこ")
    if c == 2:
        print("勝ち")
    if c == 3:
        print("負け")
elif y == 2:
    if c == 1:
        print("負け")
    if c == 2:
        print("あいこ")
    if c == 3:
        print("勝ち")
elif y == 3:
    if c == 1:
        print("勝ち")
    if c == 2:
        print("負け")
    if c == 3:
        print("あいこ")

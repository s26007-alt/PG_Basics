def float_to(s):
    """
    関数名：float_to
    引数名：ｓ：データ型：str
    戻り値：引数をfloat型に変換した値
    """
    try:
        return float(s)
    except (ValueError):
        print("数字ではないので処理を中止します")

f = float_to("Hello World")
print(f)

def f(a,b,c,y=4,z=5):
    """
    関数名：ｆ
    引数名：a　データ型：int　：必須引数
    引数名：b　データ型：int　：必須引数
    引数名：c　データ型：int　：必須引数
    引数名：y　データ型：int　：オプション引数
    引数名：z　データ型：int　：オプション引数
    戻り値：なし
    """
    result = int(a+b+c+y+z)
    print(result)

a = 1
b = 2
c = 3
f(a,b,c)

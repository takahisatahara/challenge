#4

lists = [5, 9, 13, 18]

while True:
    
    ans = input(" \n数字を当てよう！（答えは 0 から 20 の間だよ）：")
    
    if ans == "q":
        print(" \n終了します \n")
        break
    
    try:
        ans = int(ans)
    except ValueError:
        print(" \n数字を入力するか、q(小文字)で終了します")
        continue
        
    if ans in lists:
        print(" \n　正解！！！")
    else:
        print(" \n　不正解・・・")

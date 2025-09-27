'''
ユーザーから2つの正の整数値を受取り、両方とも素数であるか判定するプログラムを作成せよ。
素数である場合はTrue、素数でない場合はFalseと出力すること。
'''
'''step0:動作を考える
1. ユーザーからインプットで数字を２個入力してもらう
2. それぞれが素数か否かを判定
3. 素数・素数ならTrue、素数・not素数ならFalse

素数の定義
１とその数字以外に約数を持たない２以上の数字
ある数字の約数は、２からその数字の1/2以下の数字の範囲にある
例）
10の約数  ->  1, 2, 5, 10 (10の1/2は5)
15の約数  ->  1, 3, 5, 15 (15の1/2は7.5)
２から1/2までの数字をひとつずつ検証すれば約数か否かが判定できる

'''

# step1:数字を素数か否か判定する
num = 7
half = num // 2
for i in range(2, half+1):
  if num % i == 0:
    print(f"{num}は素数ではありません")
    break
else:
  print(f"{num}は素数です")

'''
実行結果
num = 7 の時
7は素数です
num = 12 の時
12は素数ではありません

※ポイント※
1. break を入れる
もしbreakを入れなければ、
  if num % i == 0:
      print(f"{num}は素数ではありません")
「12」を判定する場合
このループ内で割り切れる数字全てを判定し、
4かい「12は素数ではありません」と表示させる
その後、唯一割り切れた「12÷6」の結果を「else」にわたして
「12は素数です」と表示させる

2. else: の位置
if よりもひとつインデントを下げる

for i in range(2, half+1):
  if num % i == 0:
    print(f"{num}は素数ではありません")
    break
  else:
    print(f"{num}は素数です")

この位置にインデントがあった場合
  ループの範囲が「2-5」だったとき、
  一つ一つの数字の判定結果が break で終了になるまで表示され続ける
例）
数字が「7」だったときの実行結果
7は素数です ..... 7÷2の結果
7は素数です ..... 7÷3の結果
と、2回表示される

'''

# step2:判定したい数字を2かい入力させる
a = int(input("一つ目の整数値を入力："))
b = int(input("二つ目の整数値を入力："))
# a について素数を判定
a_half = a // 2
for i in range(2, half+1):
  if a % i == 0:
    print(f"{a}は素数ではありません")
    break
else:
  print(f"{a}は素数です")
  a = True

# b について素数を判定
b_half = b // 2
for i in range(2, half+1):
  if b % i == 0:
    print(f"{b}は素数ではありません")
    break
else:
  print(f"{b}は素数です")
  b = True

if a == True and b == True:
  print("True")
else:
  print("False")
'''
実行結果
a=9, b=7のとき
  一つ目の整数値を入力：9
  二つ目の整数値を入力：7
  9は素数ではありません
  7は素数です
  False

これで意図した結果になったように思うが...
判定したい数字が２と３の時は「素数ではありません」と表示される
  2は素数ではありません
  3は素数ではありません


'''
# step3:2と3を素数判定させる
a = int(input("一つ目の整数値を入力："))
b = int(input("二つ目の整数値を入力："))
# a について素数を判定
a_half = a // 2
for i in range(2, half+1):
  if a == 2 or a == 3:        # 2と3だけ例外にした
    print(f"{a}は素数です")
    a = True
    break                     # ここで break を入れないと elif で aにTrueを代入した状態で次に渡されてしまう
  elif a % i == 0:
    print(f"{a}は素数ではありません")
    break
else:
  print(f"{a}は素数です")
  a = True

# b について素数を判定
b_half = b // 2
for i in range(2, half+1):
  if b == 2 or b == 3:
    print(f"{b}は素数です")
    b = True
    break
  elif b % i == 0:
    print(f"{b}は素数ではありません")
    break
else:
  print(f"{b}は素数です")
  b = True

if a == True and b == True:
  print("True")
else:
  print("False")
'''
実行結果
a=2, b=3のとき
  2は素数です
  3は素数です
  True

'''
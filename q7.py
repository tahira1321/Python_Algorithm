'''
ユーザーから10回数字を受取り、「前回と同じ数を入力した回数」を出力、10回連続したらperfectと返すプログラムを作成せよ。
'''
'''
step0:動作を考える
10回数字を受けとる  10回連続で入力が成功するまで繰り返し入力を求められる
  →数字の入力もループに入れる

条件分岐を使用
ループ
数字を入力

条件分岐
ループ1回目 → 「連続なし」
ループ2回目以降
  → 1回目と同じとき 「n回連続」
  → 前回と異なるとき  「連続なし」  = 1回目と同じ挙動
  → 10回目  perfect!!

'''

# step1:入力された数字を取得
n = int(input("1から10の数字を入力："))
print(n)


# step2:繰り返し入力処理をさせる
for i in range(1, 3):
  n = int(input("1から10の数字を入力："))
  print(n)


# step3:入力された数字を繰り返し表示する
check_n = 0
i = 1
while i <= 10:
  n = int(input("1から10の数字を入力："))
  current_n = n
  if check_n != n:
    print("連続なし")
    break





'''
# step2:入力された数字が前回と同じか判定する
n = int(input("1から10の数字を入力："))
current_number = n
print(current_number)



# step2:条件分岐を考える
n = int(input("1から10の数字を入力："))
if 1 < n < 10:
  print("{}回連続".format(n))
elif n == 10:
  print("perfect!!")
else:
  print("連続なし")


'''
# ユーザーから数字を受けとって、受取った数字が3の倍数の時にfoo、それ以外の時はnooと出力するプログラム

# step1:1から指定した数字までを表示
num = 10
for i in range(1, num + 1):
  print(i)
print()

# step2:1からユーザーが入力し数字までを表示
num1 = int(input("好きな正の整数を入力："))
for i in range(1, num1 + 1):
  print(i)
print()

# step3:「3の倍数の時foo」、「それ以外の時noo」 → 条件分岐を使用する（もし～なら）
# 3の倍数を言いかえると「3で割った時に余りが0の数字」
num2 = int(input("好きな正の整数を入力："))
for i in range(1, num2 + 1):
  if i % 3 == 0:
    print("foo")
print()

# step4:3の倍数以外のときを指定（else）
# ※step3を実行すると「foo」しか表示されない
num3 = int(input("好きな正の整数を入力："))
for i in range(1, num3 + 1):
  if i % 3 == 0:
    print("foo")
  else: # ３の倍数以外を指定
    print("noo") # 3の倍数以外の時の表示する文字を指定
print()

# おまけ
# これでコードは完成したが、なにがnooでなにがfooかわからない。なので表示を整える
num3 = int(input("好きな正の整数を入力："))
for i in range(1, num3 + 1):
  if i % 3 == 0:
    print("{:2}:foo".format(i))
  else:
    print("{:2}:noo".format(i))
print()
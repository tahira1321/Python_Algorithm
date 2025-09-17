# 1×1～9×9の九九の段の答えを出力

# step1:1-9を表示 ※横位一列
for i in range(1, 10): #1から9までの数字を表示
  print(i, end="")
print()
print()

# step2:forの中にforをいれて、繰り返し表示する
for i in range(1, 10):
  for j in range(1, 10):
    print("{}&{}".format(i, j), end=" ") # iとjを表示
  print() # 各段ごとに改行
print()

# step3:表示を掛算の結果に変更する。加えて格段の最後尾に段を表示する。
for i in range(1, 10):
  for j in range(1, 10):
    print("{}".format(i * j), end=" ") #掛算の結果を表示
  print("「{}」の段".format(i)) # 各段ごとに改行+段を表示
print()

# step4:表示を整える
for i in range(1, 10):
  for j in range(1, 10):
    print("{:2}".format(i * j), end=" ") #表示する数字を2ケタに設定
  print("「{}」の段".format(i)) 
print()

# おまけ
for i in range(1, 10):
  for j in range(1, 10):
    print("{}×{} ={:2}".format(i, j, i * j), end="  ") #表示する数字を2ケタに設定
  print("「{}」の段".format(i)) 
print()
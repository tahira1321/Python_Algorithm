# ユーザーから2つの数字（i, j）を受取って一度出力し、iとjの中身を入替えて再度出力するプログラム
# ※出力するためのコードはprint("i =", i, ", j =", j)を必ず使用すること。

# step1:2つの数字を受けとり表示させる
i = int(input("一つ目の数字："))
j = int(input("二つ目の数字："))
print("i = {}, j = {}".format(i, j))

# このまま i = j とすると i の数字が上書きされて消えてしまう
# step2:それぞれの数字を一時的に変数へ新たな変数へ代入
i = int(input("一つ目の数字："))
j = int(input("二つ目の数字："))
print("i = {}, j = {}".format(i, j))
i_replace = i
j_replace = j
print("i_replace = {}, j_replace = {}".format(i_replace, j_replace))

# step3:i_replace -> j, j_replace -> i にそれぞれ代入
i = int(input("一つ目の数字："))
j = int(input("二つ目の数字："))
print("i = {}, j = {}".format(i, j))
i_replace = i
j_replace = j
print("i_replace = {}, j_replace = {}".format(i_replace, j_replace))
i = j_replace
j = i_replace
print("i = {}, j = {}".format(i, j))
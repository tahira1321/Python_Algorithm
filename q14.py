'''出題
バブルソートを作成せよ。
# 出力例
[6, 15, 4, 2, 8, 5, 11, 9, 7, 13] => [2, 4, 5, 6, 7, 8, 9, 11, 13, 15]
'''
'''バブルソートとは？
定義
隣接する要素同士を比較し、順序が逆であれば入れ替えることを繰り返すことで、データ列を昇順または降順に並べ替える基本的なソートアルゴリズム

仕組み
1. データ右端の2つの数字を比較し、左＞右なら入れ替える
2. 左にひとつズレて、左右を比較し左＞右なら入れ替える
3. 左端まで繰り返す → これにより小さい数字が左に動いていく
4. 次は、先頭を除いた範囲内で右から順に比較と交換を繰り返す

'''
'''基礎知識
配列
複数のデータに番号を付けてまとめて管理する「変数」
例
a = [1, 2, 3, 4, 5, 6]
  a：配列を格納する変数
  []：配列を示す記号
  要素：一つ一つのデータを「要素」という
  添え字：要素には番号が振られている。
      一つ目：[0]、2つ目[1]....n番目[n-1]
      ０からn-1までの数字が降られる
      例）データ数5個の場合
      [0], [1], [2], [3], [4]

配列のデータ数（要素数：サイズ）を取得したいとき
len()


'''


'''step0:動作を考える
[6, 15, 4, 2, 8, 5, 11, 9, 7, 13] をソート対象のデータとしたとき
1. データ数をカウント：対象データの数が数えられる範囲とは限らない
2. データ[n]とデータ[n-1]を比較
3. 条件分岐：n-1 > n のとき入れ替える
4. 次は、n と n-2 を比較する
5. 
6. 

'''


'''
# step1:配列を変数に代入し数を数える
arr = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
unsorted_arr = arr
print(len(arr))  # siza10

# step2:右端2つの要素を取得する
print(arr[9], arr[8])

# step3:要素を比較する
if arr[9] < arr[8]:
  temp = arr[9]
  arr[9] = arr[8]
  arr[8] = temp
print(arr[9], arr[8])

print("-----改行-----")

# step3:繰り返しを考える
print(arr)
size = len(arr)
print(size)
for i in range(size-1):
  for j in range(size-2, i-1, -1):
    if arr[j] > arr[j+1]:
      temp = arr[j]
      arr[j] = arr[j+1]
      arr[j+1] = temp
      # print(arr)
    # print(arr)
  # print(arr)
print(arr)
print("-----改行-----")
'''


'''
for i in range(size-1):
  sortする範囲を指定する
  [0] から [9] までの範囲

for j in range(size-2, i-1, -1):
  sort判定する範囲を指定
  実際の範囲を数値にする
  i = 0
    size-2 -> 10-2 -> 8
    i-1 -> 0-1 -> -1
    つまり、 8 から 0 まで -1 ずつ変化する

if arr[j] > arr[j+1]:
  具体的にインデックスを見てみる
  arr[j] -> arr[8]
  arr[j+1] -> arr[9]

temp = arr[j]
  temp -> 「temporary:一時的な」 の略
  arr[j] を一時的な変数に代入して逃がす

arr[j] = arr[j+1]
  arr[j] に arr[j+1] を代入

arr[j+1] = temp
  arr[j+1] に temp(代入前のarr[j])を代入

'''

# step4:sort前とsort後の配列を同時に表示させたい
'''
sort前とsort後の配列を同時に表示するには、sort後の結果をreturnで取得して変数に代入したい
'''
a = 10
a_base = a
a = 5
print(f"{a_base} -> {a}")

arr = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
# unsorted_arr = arr
# print(f"1:{unsorted_arr}")
size = len(arr)
def bubble_sort(arr):
  for i in range(size-1):
    for j in range(size-2, i-1, -1):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
  return arr
sorted_arr = bubble_sort(arr.copy())
print(f"{arr} -> {sorted_arr}")
'''
sorted_arr = bubble_sort(arr.copy()) に関して
  この記述は、元の配列をコピーしたものを引数としている
  Gitのbranchのようなものかな

  これが、sorted_arr = bubble_sort() の記述の場合、
  元の配列を編集する
  最後に print(arr) の結果が、sort後の配列が表示されてしまう
'''
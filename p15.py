'''
マージソートを作成せよ。
# 出力例
[6, 15, 4, 2, 8, 5, 11, 9, 7, 13] => [2, 4, 5, 6, 7, 8, 9, 11, 13, 15]
'''
'''
マージソートとは？
既に整列してある複数個の列を1個の列にマージする際に、小さいものから先に新しい列に並べれば、新しい列も整列されている、というボトムアップの分割統治法

流れ
整列したい対象のデータを二分する
要素がひとつになるまで二分を繰り返す
分割した要素同士を並べかえながら戻していく
'''

# step1:データを二分する
print("---step1---")
arr = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
n = len(arr)
half = n//2
arr1 = arr[:half] # [6, 15, 4, 2, 8]
arr2 = arr[half:] # [5, 11, 9, 7, 13]
print(arr1)
print(arr2)

n = len(arr1)
half = n // 2
arr3 = arr1[:half]
arr4 = arr1[half:]
print(arr3) # [6, 15]
print(arr4) # [4, 2, 8]

n = len(arr2)
half = n // 2
arr5 = arr2[:half]
arr6 = arr2[half:]
print(arr5) # [5, 11]
print(arr6) # [9, 7, 13]

# step2:要素の数が「1」であることを判断する
print("---step2---")
arr = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
my_arr = arr.copy()
print(my_arr)
size = len(my_arr)
if size == 1:
  print(f"{my_arr}の要素は1つです")
else:
  middle = len(my_arr) // 2
  left_half = my_arr[:middle]
  right_half = my_arr[middle:]
print(left_half)
print(right_half)

# 解答例
print("---検証用---")
# arr = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
arr = [8, 6, 4, 7]
def merge_sort(arr):
  if len(arr) <= 1:         # 要素数が0か1の時は分割不要
    return arr
  
  mid_idx = len(arr) // 2
  left_arr = arr[:mid_idx]
  right_arr = arr[mid_idx:]
  print(f"L1:{left_arr}")
  print(f"R1:{right_arr}")

  merge_sort(left_arr)      # 分割した要素を更に分割したい（再帰関数）
  merge_sort(right_arr)     # 分割した要素を更に分割したい（再帰関数）

  left_idx = right_idx = idx = 0
  while left_idx < len(left_arr) and right_idx < len(right_arr):
    print(f"nL1:{left_idx}")
    print(f"sL1:{len(left_arr)}")
    print(f"nR1:{right_idx}")
    print(f"sR1:{len(right_arr)}")
    print(f"idx1:{idx}")
    if left_arr[left_idx] <= right_arr[right_idx]:
      print(f"L2:{left_arr}")
      print(f"R2:{right_arr}")
      arr[idx] = left_arr[left_idx]
      print(f"A1{arr}")
      left_idx += 1
      print(f"nL2:{left_idx}")
    else:
      print(f"L3:{left_arr}")
      print(f"R3:{right_arr}")
      arr[idx] = right_arr[right_idx]
      print(f"A2{arr}")
      right_idx += 1
      print(f"nR2:{right_idx}")
    idx += 1
    print(f"idx2:{idx}")

  while right_idx < len(right_arr):
    print(f"nR3:{right_idx}")
    print(f"sR2:{len(right_arr)}")
    arr[idx] = right_arr[right_idx]
    print(f"A3{arr}")
    idx += 1
    right_idx += 1
  
  while left_idx < len(left_arr):
    print(f"nL3:{left_idx}")
    print(f"sL2:{len(left_arr)}")
    arr[idx] = left_arr[left_idx]
    print(f"A4{arr}")
    idx += 1
    left_idx += 1
  return arr
print(merge_sort(arr))
'''自分の頭で理解する
1. def merge_sort(arr):
    def:関数を定義
    merge_sort:関数名
    (arr):引数

    関数の書き方
    def 関数名(引数):
      処理
      return 

2. if len(arr) <= 1:      もし len(arr):配列arrの要素数 が 1以下の時
    return arr            戻り値：arr を結果として返して、処理を終了する
    例）
    arr = [6] の時 -> 実行結果 [6]
    arr = [] の時 -> 実行結果 [] (要素が空)

3.  mid_idx = len(arr) // 2         mid_idx:中央の要素番号 = 配列arr の全要素数の半分
    left_arr = arr[:mid_idx]        変数left_arr に arr[:mid_idx]を代入
    right_arr = arr[mid_idx:]       変数right_arr に arr[mid_idx:]を代入
      :mid_idx の ":" は「スライド」
      arr[:mid_idx] の場合、[0] ～ [mid_idx]未満 の配列     len(arr)=>10 且つ mid_idx=>5 の時、[0] - [4]
      arr[mid_idx:] の場合、[nid_idx] ～ [n-1]まで の配列   len(arr)=>10 且つ mid_idx=>5 の時、[5] - [9]

4.  merge_sort(left_arr)      引数left_arr つまり arr[:mid_idx]([0] - [4]) 自体を 関数merge_sort の引数に渡している <= 再帰関数
    merge_sort(right_arr)     引数right_arr つまり arr[mid_idx:]([5] - [9]) 自体を 関数merge_sort の引数に渡している <= 再帰関数
      例） arr = [8, 6, 4, 7] の時
      まずは、要素がひとつになるまで分割が繰り返される(再帰関数)
        -> left_arr=[8, 6], right_arr=[4, 7] -> left_arr=[8], right_arr=[6], left_arr=[4], right_arr=[7]

5.  left_idx = right_idx = idx = 0
    left_idx と right_idx と idx と に初期値0を代入
    つまり  left_idx = [0]
            right_idx = [0]
            idx = [0]

6. while left_idx < len(left_arr) and right_idx < len(right_arr):
    left_idx:(初期値0) が len(left_arr):([0] ～ [4]) までの5個未満
    且つ
    right_idx:(初期値0) が len(right_arr):([5] ～ [9]) までの5個未満
    の間、処理が繰り返される
    配列の要素が全て分割され、ひとつの要素になった段階でループが発動する

7.  if left_arr[left_idx] <= right_arr[right_idx]:
      arr[idx] = left_arr[left_idx]
      left_idx += 1
    else:
      arr[idx] = right_arr[right_idx]
      right_idx += 1
    idx += 1
    例） arr = [8, 6, 4, 7] の時
      left_arr=[8, 6] が left_arr=[8] と right_arr=[6] に分割された時点で
      right_arr=[4, 7] が分割されるのを待たずに、left_arr=[8] と right_arr=[6] を比較する
      <左：arr[0]=8, 右：arr[0]=6>
      左 <= 右(left_arr[left_idx] <= right_arr[right_idx]) を満たさないため else へ移動
      左 > 右 であり、arr[idx] = right_arr[right_idx] が適応され、arr[0] に「6」が代入される
      右側の要素が代入されたので、right_idx += 1 が実行され right_idx が 0 -> 1 へ加算される
      最後に idx += 1 実行され、idx が 0 -> 1 へ加算される

8. while left_idx < len(left_arr):
    右：arr[0]=6 が代入され、 左：arr[0]=8 が比較対象を失う 
    左側の要素：left_idx は自身の要素数と比較する
    インデックス"0" < 要素数"1" を満たす

9.  arr[idx] = left_arr[left_idx]
    idx += 1
    left_idx += 1
    arr の要素の2番目 idx[1] に左：arr[0]=8 が代入され
    arr [6, 8, , ] となる 
    idx += 1 が実行され、idx[2] となる
    left_idx += 1 が実行され、left_idx[1] となる

10. [4, 7] -> 左：[4], 右：[7] へ分割される
    左 < 右 であり
    left_arr[left_idx] <= right_arr[right_idx] が適応される 
      arr[idx] = left_arr[left_idx]
      idx[2] に "4"が代入される
      left_idx += 1


11. while right_idx < len (right_arr):
      arr[idx] = right_arr[right_idx]
      idx += 1
      right_idx += 1



12. 




13. 





14. 





15. 

'''

print("---完成形---")
arr = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
my_arr = arr.copy()
def merge_sort(my_arr):
  if len(my_arr) <= 1:
    return my_arr
  
  mid_idx = len(my_arr) // 2
  left_arr = my_arr[:mid_idx]
  right_arr = my_arr[mid_idx:]

  merge_sort(left_arr)
  merge_sort(right_arr)

  left_idx = right_idx = idx = 0
  while left_idx < len(left_arr) and right_idx < len(right_arr):
    if left_arr[left_idx] <= right_arr[right_idx]:
      my_arr[idx] = left_arr[left_idx]
      left_idx += 1
    else:
      my_arr[idx] = right_arr[right_idx]
      right_idx += 1
    idx += 1

  while right_idx < len(right_arr):
    my_arr[idx] = right_arr[right_idx]
    idx += 1
    right_idx += 1
  
  while left_idx < len(left_arr):
    my_arr[idx] = left_arr[left_idx]
    idx += 1
    left_idx += 1
  return my_arr
print(f"変更前{arr} -> 変更後{my_arr}")
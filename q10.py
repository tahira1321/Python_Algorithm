'''
九九
for while それぞれで解く
'''
# for
for i in range(1, 10):
  for j in range(1,10):
    print(f"{i}×{j}={i*j:2}")

# while
i = 0
while i < 9:
  i += 1
  j = 0
  while j < 9:
    j += 1
    print(f"{i}×{j}={i*j:2}")
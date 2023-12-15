from typing import Any

num = [6, 3, 8, 0, 2 , 4, 8, 2, 7, 8, 11, 9, 5, 3, 2, 5, 6, 7]

max = num[0]
for i in num: 
    if i > max:
        max = i
print(max)
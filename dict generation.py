num = [1, 2, 3, 'f', True]

res  = {y: y if type(y) == str or type(y) == bool else y**2 for y in num}
print(res)

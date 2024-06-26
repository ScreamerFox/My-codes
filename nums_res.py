import random

nums1 = []
while len(nums1) <= 20:
    nums1.append(random.randint(-20, 100))

print(nums1)


def max_list_def(nums):              # функция которая находит максимальное число в списке
    max_n = 0
    for i in nums:
        if i > max_n:
            max_n = i
    print(max_n, '- максимальное число')

def num_ch(nums):
    num_l = []
    for i in nums:
        if i % 2 != 0:
            num_l.append(i)
    return print(len(num_l), '- Чётных чисел')


def unique_list(u_nums):
    unique_ = []
    for i in u_nums:
        if i not in unique_:
            unique_.append(i)
    print(len(unique_), '- уникальных элементов, из 20', )


max_list_def(nums1)
num_ch(nums1)
unique_list(nums1)

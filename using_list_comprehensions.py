m = [x ** 2 for x in range(5)]
print(m)  # [0, 1, 4, 9, 16]

# finding common numbers from two lists using list comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num)  # [2, 3, 4]

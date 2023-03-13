# # 1 Find the sum of this Tuple using while loop test_tup = (15, 20, 123, 47, 26, 81)
# test_tup = (15, 20, 123, 47, 26, 81)
# acc = 0
# for num in test_tup:
#     acc += num
# print(acc)

# # 2 Find the largest number in this Tuple test_tup = (15, 20, 123, 47, 26, 81)
# test_tup = (15, 20, 123, 47, 26, 81)
# print(max(test_tup))

# #3 Find the sum of all integer numbers in this Tuple
# test_tup = ([17, 28], [93, 11], [20, 17])
# flat_tuple = tuple(sum(test_tup, []))
# acc = 0
# for num in flat_tuple:
#     acc += num
# print(acc)

#4 Sort this Tuple by the list total
input_tup = ([2, 20], [44, 1], [3, 13])
# sorted_tup should be  ([3, 13], [2, 20], [44, 1])
sorted_tup = sorted(input_tup,key=sum)
print(sorted_tup)
empty_list = []
list1 = [1,7,2,0,4]
print(list1)
list2 = list1 * 2
print("List printed twice: ", list2)
listlen = len(list1)
print("length of the list: ", listlen)
print("A few index values: ")
print(list1[1], list1[-3])
print("A portion of the list and reversed: ")
print(list1[0:3])
print(list1[::-1])
if list1[0] == list1[4]:
    print("The first and last digits match")
else:
    pass
average = sum(list1) / len(list1)
print("The average is: ", average)
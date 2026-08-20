snack_box1 = {"orange", "fruit punch", "cookie", "one dorito chip", "apple"}
snack_box2 = {"cookie", "one dorito chip", "ice cream", "orange"}
print("Snack box 1:", snack_box1)
print("Snack box 2:", snack_box2)

snack_box1.add("banana")
print("Snack Box 1 after adding banana:", snack_box1)
bothsnackbox = snack_box1.intersection(snack_box2)
print("Snacks in both boxes:", bothsnackbox)

import array as arr
Snakcount = arr.array('i', [9, 5, 1, 5])
print("Snack counts array:", Snakcount)

Snakcount.insert(3, 2)
Snakcount.append(100000)
print("Snack counts after adding items:", Snakcount)
Count5 = Snakcount.count(5)
print("Number of times 5 appears:", Count5)
Snakcount.reverse()
print("Reversed snack counts array:", Snakcount)

print("SNACK COUNTER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)
print("Shared snacks:", bothsnackbox)
print("Snack counts:", Snakcount)
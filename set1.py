basket1 = {"apple", "banana", "apple", "grape"}
basket2 = {"banana", "mango", "grape", "banana"}
print("basket1: ", basket1)
print("basket2: ", basket2)
basket1.add("peach")
print("basket1: ", basket1)
basket3 = basket1.intersection(basket2)  
print("basket3: ", basket3)
import array as arr
fruit_counts = arr.array("i",[2, 9, 4, 6, 9])
print("fruit count array: ", fruit_counts)
fruit_counts.insert(2, 12)
print(fruit_counts)
fruit_counts.append(1)
print(fruit_counts)
count_of_9 = fruit_counts.count(9)
print("How many times 9 appears: ", count_of_9)
fruit_counts.reverse()
print(fruit_counts)
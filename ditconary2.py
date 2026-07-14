test_dict = {"Codingal": 2, "Is": 2, "Best": 2, "For": 2, "Coding": 1}
print(test_dict)
K = 2
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1
    print("The frequency of K is: " + str(res))
# Tanaya's problem
T = int(input("Enter a count:"))
lst = []
for i in range(0, T) : lst.append(input("Enter the text:"))
for str in lst :
    str_1 = ""
    str_2 = ""
    for a in range(len(str)) :
        if a%2 == 0 : str_1 += str[a]
        else : str_2 += str[a]
    print(str, "=", str_1, str_2)
# Question number -1
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    try :
        if i <= 150 :
            if i % 5 == 0 : print(i)
    except : quit()#
#Question number -2
import re
num= input("Enter the number : ")
b = re.findall("[0-9]", num)
print("The total number of digits are : ", len(b))
# Question number -2 Alternative way
num = input("Enter the number: ")
print("The total number of digits are : ", len(num))
# Question number -2 Using while loop
numb = int(input("Enter the number : "))
count = 0
while (numb > 0) :
    count+=1
    numb//=10
    print("The total number of digits are : ")
# Question number -3
list1 = [10, 20, 30, 40, 50]
lst = []
for i in range(len(list1)-1, -1, -1): lst.append(list1[i])
print("Done", lst)
# Question number –3
list1 = [10, 20, 30, 40, 50]
list1.sort(reverse=True)
print(list1)
# Question number -4
for i in range(1, 6):
    for l in range(1, i+1):  print(l, end="")
    print(sep="/n")
# List comprehensions Question 1
lst = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print([i for i in lst if i%5 == 0])
# Question 2 - Using numpy
m = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
import numpy as np
print(np.transpose(m))
# Question 2 - Using the normal way
print([[m[j][i] for j in range(len(m))] for i in range(len(m[0]))])
# Question 3
input = [5, 6, 7, 8, 9]
print([i**2 for i in input])
# Question 4
lst1 = [9, 8, 2, 1, 1]
lst2 = [1, 4, 1, 1, 2]
a = set(lst1)
b = set(lst2)
if(a & b) : print(a & b)
# Question 4 The other way
print([x for x in lst1 if x in lst2])
# Question 5 Using regex
import re
x = "Watashi na kita, orewa zettai da"
print(re.findall("[^ aeiouAEIOU]", x))
# Question 5
y = ["a", "e", "i", "o", "u", " "]
print([i for i in x if i not in y])
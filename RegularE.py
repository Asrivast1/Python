# split() creates a list of the the lines of the files
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for lines in fh:
    line = lines.split()
    for element in line:
        if element not in lst : lst.append(element)
print(lst.sort())
# Using the range function
friends = ['Joseph', 'Glenn', 'Sally']
print(range(len(friends)))
# THe functions within the list can be invoked using dir()
x = list()
print(type(x))
print(dir(x))
# Double Slit Pattern
line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
# Dictionary Basics
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2 # Dictionary's values are mutable
print(purse)
# get() creates a dictionary out of a list with numbers indicating their occurences
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names : counts[name] = counts.get(name, 0) + 1
print(counts)
# Word count
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:counts[word] = counts.get(word,0) + 1
print('Counts', counts)
# Properties of dictionaries
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())
# Tuples are immutable, reverse(), sort() and append() doesn't works on it
t = ()
dir(t)
(x, y) = (4, 'fred') # Tuples can be compared
print(y)
# Sort by values instead of keys
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() : tmp.append( (v, k) )
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
# A shorter version
c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )
# Using re.search()
import re
hand = open('Regex')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) : print(line)
# Using findall expression
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[0-9]',x)
print(y)
#
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
#
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
#
x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall('\S+@\S+',x)
print(y)
#
y = re.findall('^From (\S+@\S+)',x)
print(y)
#
x = 'We just received $10.00 for cookies.' # + means atleast one or more
y = re.findall('\$[0-9.]+',x) # \$ means - A real dollar sign
print(y) # Contents inside and including [] means - A digit or period

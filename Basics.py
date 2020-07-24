# Looping through strings
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
# Looping and counting in strings
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' : count = count + 1
print(count)
# String operations
stuff = 'Hello world'
print(type(stuff)) # Returns the data type
print(dir(stuff)) # Prints the properties
# Iterations - Pay attention to the usage of break and continue statement
while True:
    line = input('> ')
    if line[0] == '#' :continue
    if line == 'done' :break
    print(line)
print('Done!')
# Defining Pay
def computepay(h,r):
    if  h>40:
        reg=r*h
        otp=(h-40.0)*(r*0.5)
        xp=reg+otp
    else:xp=h*r
    return xp
hrs = input("Enter Hours:")
hr = float(hrs)
fh = input("Enter Rate:")
fr = float(fh)
p = computepay(hr,fr)
print("Pay",p)
# Calculating the largest and smallest from the given number
largest = None
smallest = None
while True:
    try:
         num = input("Enter a number: ")
         if num == "done" :break
         ank = int(num)
         if largest is None or ank>largest : largest = ank
         elif smallest is None or ank<smallest : smallest = ank
    except:
         print('Invalid input')
         continue
print("Maximum is", largest)
print('Minimum is', smallest)
# Slicing the float
text = "X-DSPAM-Confidence:    0.8475"
kuch = text.find('0')
bhi = float(text[kuch:])
print(bhi)
# File Handling
fname = input('Enter the file name:  ')
try : fhand = open(fname)
except:
      print('File cannot be opened:', fname)
      quit()
count = 0
for line in fhand:
      if line.startswith('Subject:') : count = count + 1
print('There were', count, 'subject lines in', fname)
# Reading through a file
fhand = open('mbox-short.txt')
inp = fhand.read() # It converts the file into a big blob of text with /n and all
print(len(inp))
# Reading through a file and placing the conditioning to print out the emails and their count
fhand = open("mbox-short.txt")
count = 0
for line in fhand:
    words = line.rstrip().split()
    if words[0] != "From": continue
    print(words[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
# Reading through the file and finding the maximum occurrences
fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
hand = open(fname)
lst = list()
for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])
counts = dict()
for word in lst : counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print (bigword,bigcount)
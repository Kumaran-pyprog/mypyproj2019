print("Highest num from list")
import random
import numpy as np
#user_input=[int(user_input) for user_input in input("Enter the 7 num to find highests").split()]
listval=[]
for i in range(1):
    for rand in range(10,1000,75):
        listval.append(rand)
print("To show all list val:\n",listval)
#covert to set
list_val=list(set(listval))
print("unordered list:\n",list_val)

#find the largest  element from a list
max=list_val[0]
sec_max=list_val[0]
third_max=list_val[0]
for i in list_val:
    if i>max:
        max=i
print("largest element is:",max)
print("second largest element:")
for i in list_val:
    if i >sec_max and i< max:
        sec_max=i
print("second largest element:",sec_max)
print("Third largest element:")
for i in list_val:
    if i >third_max and i< sec_max:
        third_max=i
print("second largest element:",third_max)
print("Smallest num from list")
min=list_val[0]
sec_min=list_val[0]
third_min=list_val[0]
for i in list_val:
    if i<min:
        min=i
    elif i<sec_min and i>min:
        sec_min=i
    elif i<third_min and i>min:
        third_min=i
print("smallest element:",min)
print("smallest element:",sec_min)
print("smallest element:",third_min)
print("Remove duplicates element from given string:")
user_input=input("Enter the string val and remove duplicate val:")#qspiders
d={}
for i in user_input:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
for k,v in d.items():
    print("char {} present {} times".format(k,v))
#remove duplicate char
list_val=list(set(user_input))
print(list_val)
d={}
for i in list_val:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print("After removing duplicates from input string")
for k,v in d.items():
    print("char {} present {} times".format(k,v))
#another methods
#input:x=Qspiders
#output:Qspiders
x='qspiders'
y='s'
if x.endswith(y):
    res=x[:-len(y)]
print("after removing the string val is ",res)
x='Qspiders'
y='located at BTM'
print(x,''.join(y))
print(x +" "+ y)
#print(z)
#how to convert int to binary
x=12
y=bin(x)

print("converting int to bin:",y)
print("converting bin to int",int(0b1100))
#how to convert binary string to int
print("converting bin string to int base 2:",int('0b1100',2))
#print("converting bin string to int base 8:",int('0b11000000',8))
#print("converting bin string to int base 10:",int('0b1100',10))
#how to change the bits using bitwise operator
x=12
print("leftshift x<<1:",x<<1)
print("leftshift x>>1:",x>>1)
print("converts int to bin:",bin(x))
print("converts shift operator val to bin bin(x<<1):",bin(x<<1))
print("converts shift operator val to bin bin(x>>1):",bin(x>>1))
#x<<2
print("leftshift x>>2:",x<<2)
print("leftshift x>>2:",x>>2)
print("converts int to bin:",bin(x))
print("converts shift operator val to bin bin(x<<2):",bin(x<<2))
print("converts shift operator val to bin bin(x>>2:",bin(x>>2))
#x<<2
print("leftshift x<<3:",x<<3)
print("leftshift x>>3:",x>>3)
print("converts int to bin:",bin(x))
print("converts shift operator val to bin bin(x<<3):",bin(x<<3))
print("converts shift operator val to bin bin(x>>3):",bin(x>>3))
print("setting a bit:")
num=12
offset=1
mask=1<<offset
set_bit=num|mask
print("set a bit(12|(1<<1):",set_bit)
offset=2
mask=1<<offset
set_bit=num|mask
print("set a bit(12|(1<<2):",set_bit)
offset=3
mask=1<<offset
set_bit=num|mask
print("set a bit(12|(1<<3):",set_bit)
print("clearing a bit:")
num=12
offset=1
mask=~(1<<offset)
clear_bit=num & mask
print("clearing a bit(12&(~(1<<1):",clear_bit)
offset=2
mask=~(1<<offset)
clear_bit=num & mask
print("clearing a bit(12&(~(1<<2):",clear_bit)
offset=3
mask=~(1<<offset)
clear_bit=num & mask
print("clearing a bit(12&(~(1<<3):",clear_bit)
print("Toggling bit:")
num=12
offset=1
mask=1<<offset
toggle_bit=num^mask
print("toggle bit(num^(1<<1):",toggle_bit)
offset=2
mask=1<<offset
toggle_bit=num^mask
print("toggle bit(num^(1<<2):",toggle_bit)
offset=3
mask=1<<offset
toggle_bit=num^mask
print("toggle bit(num^(1<<3):",toggle_bit)
#take the example of 0x01fc
set_bit=hex(0x01fd|(1<<1))
print("settbit(0x01fc|(1<<1):",set_bit)
clear_bit=hex(0x01fc&(~(1<<1)))
print("clear bit(0x01fc&(~(1<<1)):",clear_bit)
toggle_bit=hex(0x01fc^(1<<1))
print("Toggle bit(0x01fc^(1<<1)):",toggle_bit)
#0000 00001 1111 1101==>01fd
#print(hex(0b0000000111111101))
bit_changed=hex(0x01fd|(1<<13))
print("0x01fd|(1<<13):",bit_changed)
print("binary val of 0x021fd:",bin(0x21fd))#0b10000111111101===>13th bit is 1

bit_changed=hex(0x01fd|(1<<10))
print("0x01fd|(1<<10):",bit_changed)
print("binary val of 0x05fd:",bin(0x05fd))#0b10111111101

bit_changed=hex(0x01fd|(1<<11))
print("0x01fd|(1<<11):",bit_changed)
print("binary val of 0x11fd:",bin(0x9fd))#0b1010111111101
print("set the bit:")
#set the bit
bit_changed=hex(0x01fd|(1<<11)|(1<<10)|(1<<9))
print("0x01fd|(1<<11)|(1<<10)|(1<<9):",bit_changed)
print("binary val of 0x0ffd:",bin(0x0ffd))#0b111111111101
print("clear the bit:")
#clear the bit
bit_changed=hex(0x01fd&(~(1<<11|1<<10|1<<9)))
print("(0x01fd&(~(1<<11|1<<10|1<<9)):",bit_changed)
print("binary val of 0x01fd:",bin(0x01fd))#

print("Toggle the bit:")
#Toggle the bit
bit_changed=hex(0x01fd^(1<<11|1<<10|1<<9))
print("0x01fd^(0x01fd^(1<<11|1<<10|1<<9)):",bit_changed)
print("binary val of 0x0ffd:",bin(0x0ffd))#0b111111111101

print("set,clear and toggle the differenet bits:")
bit_changed=hex(0x01fd|(0<<11|1<<10|0<<1)|0x01fd^(1<<14|1<<13|1<<12))
print("(0x01fd|(0<<11|1<<10|1<<1)|0x01fd&(~(1<<1))|0x01fd^(1<<14|1<<13|1<<12):",bit_changed)
print("binary val of 0x75fd:",bin(0x75fd))#0b111111111101





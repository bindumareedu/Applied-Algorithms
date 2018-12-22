import time
from decimal import *
import matplotlib.pyplot as plt
#decimal.getcontext().prec = 3

#Implementing Bubble Sort on List sent through arguments
def sort_my(list1):
    for i in range(0, len(list1)):
        for j in range(0, len(list1)-i-1):
            if (list1[j] > list1[j+1]):
                #list1[j], list1[j + 1] = list1[j + 1], list1[j]
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    #for i in range(len(list1)):
     #   print(list1[i])
    #print("--------------------------------")

def importing(f,list1,i):

    #list1.clear()
    count=0
    for line in f:
        list1.insert(count, line.rstrip('\n').rstrip())
        count = count + 1
        if count + 1 == int(i):
           break;
    calruntime(list1)

def calruntime(list1):
    list1 = [int(x) for x in list1]
    s1: decimal = time.process_time()
    sort_my(list1)
    e1: decimal = time.process_time() - s1
    s2: decimal = time.process_time()
    sort_my(list1)
    e2: decimal = time.process_time() - s2
    s3: decimal = time.process_time()
    sort_my(list1)
    e3: decimal = time.process_time() - s3
    #t[j] = int(e1[j] - s1[j])
    avg: decimal = round((e1+e2+e3)/3, 3)
    y.append(avg)



f = open("input.txt", "r")
list1 = []
y = []
x = []
value = 500

for i in range(20):
    x.append(value)
    value = value+500
i=500
while(i<=10000):
    importing(f,list1,i)
    i = i+500
#plt.xlim(500,10000,500)
#plt.ylim(0,9)
#below two for loops are for my reference
k = 0
for k in range(len(x)):
    print(x[k])
k = 0
for k in range(len(y)):
    print(y[k])
plt.plot(x, y, 'xb-')
plt.show()
print('done')




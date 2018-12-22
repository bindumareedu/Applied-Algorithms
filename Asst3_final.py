import time
from decimal import *
import matplotlib.pyplot as plt
import math


#''''''''''''''''''''' Merge Sort''''''''''''''''''#
def merge(left, right):
    """ Function to merge two arrays """
    sorted_Array = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            sorted_Array.append(left[0])
            left.remove(left[0])
        else:
            sorted_Array.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        sorted_Array += right
    else:
        sorted_Array += left
    return sorted_Array



def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        mid = len(x) // 2
        middle = math.ceil(mid)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a, b)

#''''''''''''''''''''' Median of Medians'''''''''''''''''''''#

def Median(temp_list, n):
    # temp_list contains (total elements - l+i*5) elements, so splicing it to 5 or n%5 elements
    array = temp_list[:n]
    array.sort()

    median = int(n / 2)
    # median is returned
    return array[median]


def medianofMedians(temp_list, left, right):
    # value of n is number of elements
    n = right - left + 1

    median = []

    i = 0

    # carrying out for loop for (total_elements/5) times
    for i in range(0, int(n / 5)):
        vag = Median(temp_list[(left + i * 5):], 5)
        # appending medians of every single divisions into median variable
        median.append(vag)

    # in case we remaining number of elements are less than 5
    if (i * 5 < n and n % 5 != 0):
        vag2 = Median(temp_list[(left + i * 5):], n % 5)

        median.append(vag2)
        i = i + 1

    # if value of i is 0 or 1 i.e. median array has 1 variable, then midofMed will have that variable
    if (i == 1):
        midOfMed = median[i - 1]

    if (i == 0):
        midOfMed = median[i]

    # in case median array has more than 1 elements, function is called again
    if (i > 1):
        midOfMed = medianofMedians(median, 0, i - 1)

    return (midOfMed)


#''''''''''Avg time claculation for Median of Medians'''''''''#
def runtime_moM(temp_list):
    t1 = []
    maximum=[]
    for p in range(0,3):
        s1: decimal = time.process_time()
        result=medianofMedians(temp_list, 0, (len(temp_list)-1))
        e1: decimal = time.process_time()
        t1.append(e1-s1)
    average=sum(t1)/3
    print("median of medians = ")
    print(result)
    return average



#''''''''''Average time calculation for Merge Sort'''''''''#
def runtime_mergesort(temp_list):
    temp_list = [float(x) for x in temp_list]
    t1 = []
    for p in range(0,3):
        s1: decimal = time.process_time()
        mergesort(temp_list)
        e1: decimal = time.process_time()
        t1.append(e1-s1)
    average=sum(t1)/3
    return average

#''''''''''''''''Main Function''''''''''''''''#
x1 = []
y1 = []
y2 = []
complete_list = []
temp_list = []
f = open("input.txt", "r")
#Copying all the elements from file to a list
for line in f:
    complete_list.append(line.rstrip('\n').rstrip())
counter=5000
#while (counter <= len(complete_list)-50000):
while (counter <= 100000):

    temp_list.extend(complete_list[:counter])
    temp_list = [int(x) for x in temp_list]
    print("n=", len(temp_list))
    y1.append(runtime_mergesort(temp_list))
    y2.append(runtime_moM(temp_list))
    temp_list.clear()
    counter=counter+5000
value = 5000
for i in range(0,20):
    x1.append(value)
    value = value+5000
print('its done')
plt.plot(x1, y1,"xb-", color='red')
plt.plot(x1,y2,'xb-', color='blue')
plt.ylabel("time")
plt.xlabel("input size")
plt.show()


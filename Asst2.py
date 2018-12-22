#import maxint
#from sys
#import maxint
import time
from decimal import *
import matplotlib.pyplot as plt
global low,high,leftindex,rightindex


#''''''''''Divide and Conquer'''''''''#
def Dnc(temp_list, l, h):
    global low
    global high
    global dnclow
    global dnchigh
    global maximum
    sm = 0
    left_sum = -1000000
    # Base Case: Only one element
    if (l == h):
        return temp_list[l]

        # Find middle point
    m = (l + h)//2
    maxleftsum,low1,end1=Dnc(temp_list, l, m)
    maxrightsum,low2,end2=Dnc(temp_list, m + 1, h)
    #maxCrossingSum(temp_list, l, m, h)
    for i in range (m,l-1,-1):
        sm = sm + temp_list[i]
        if(sm > left_sum):
            left_sum = sm
            low=i
    sm = 0
    right_sum = -1000000
    for j in range(m + 1, h + 1):
        sm = sm + temp_list[j]
        if (sm > right_sum):
            right_sum = sm
            high = j

    maximum =max(maxleftsum,maxrightsum,left_sum+right_sum)
    if(maximum==maxleftsum):
        dnclow=low1
        dnchigh=end1
    if(maximum==maxrightsum):
        dnclow=low2
        dnchigh=end2
    else:
        dnclow=low
        dnchigh=high
    return maximum,dnclow,dnchigh

#''''''''''Avg time claculation for Divide and Conquer'''''''''#
def calruntime2(temp_list):
    t1 = []
    maximum=[]
    for p in range(0,3):
        s1: decimal = time.process_time()
        Dnc(temp_list, 0, len(temp_list)-1)
        e1: decimal = time.process_time()
        t1.append(e1-s1)
    print("DIVIDE & CONQUER: elements", len(temp_list),"max:",maximum,"left:", dnclow, "right:", dnchigh)
    average=sum(t1)/3
    return average


#''''''''''Divide and Conquer'''''''''#
def BruteForce(temp_list,size):
    global leftindex
    global rightindex
    maxsum=-100000

    for i in range (0,len(temp_list)):
       currentsum = 0
      # maxsum+= temp_list[i]
       for j in range(i,len(temp_list)):
            currentsum+=temp_list[j]
            if(currentsum>=maxsum):
               maxsum=currentsum
               leftindex=i
               rightindex=j
    return maxsum

#''''''''''Average time calculation for Brute Force'''''''''#
def calruntime1(temp_list):
    temp_list = [int(x) for x in temp_list]
    t1 = []
    for p in range(0,3):
        s1: decimal = time.process_time()
        maxsum=BruteForce(temp_list, len(temp_list))
        e1: decimal = time.process_time()
        t1.append(e1-s1)
    print("BRUTEFORCE: elements", len(temp_list),"max:",maxsum,"left:", leftindex, "right:", rightindex)
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
counter=500
#while (counter <= len(complete_list)-50000):
while (counter <= 10000):

    temp_list.extend(complete_list[:counter])
    temp_list = [int(x) for x in temp_list]
    y1.append(calruntime1(temp_list))
    y2.append(calruntime2(temp_list))
    temp_list.clear()
    counter=counter+500
value = 500
for i in range(0,20):
    x1.append(value)
    value = value+500
print('its done')
plt.plot(x1, y1, color='red')
plt.plot(x1,y2,color='blue')
plt.ylabel("time")
plt.xlabel("input size")
plt.show()


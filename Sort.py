import random
import secrets 
import timeit
from collections import Counter

#Function to make a random list with the random method.
def randomizedList(elements, range1, range2):
    tempList = []
    x = 0
    while x < elements:
        tempList.append(random.randrange(range1, range2))
        x += 1
    return tempList

#Function to make a random list with the secrets method.
def secretizedList(elements, range1, range2):
    tempList = []
    x = 0
    while x < elements:
        tempList.append(secrets.choice(range(range1,range2)))
        x += 1
    return tempList
    
#Creating both a random list and a secret list
randomlist = []
secretlist = []

#Putting random values into random list and secret list, using random for randomlist and secrets for secretlist
randomlist = randomizedList(100, 1, 17)
secretlist = secretizedList(100, 1, 17)
#Printing both lists
print("Printing both randomized lists:")
print(randomlist)
print(secretlist)

#Counting how many times each element appears in each list.
print("Counting the amount of an element in each list and printing it out:")
secretcounter = Counter(secretlist)
print("Secrets", secretcounter)
randomcounter = Counter(randomlist)
print("Random", randomcounter)

#They both seem equally random.
print("Both methods seem equally random to me.")

#Resetting the lists to replace them with random numbers from 1-65535
randomlist = []
secretlist = []

randomlist = randomizedList(100, 1, 65536)
secretlist = secretizedList(100, 1, 65536)

#Counting how many times each element appears in each list.
print("Printing out the count of each element when the lists are 100 elements from 1-65535:")
secretCounterBig = Counter(secretlist)
print("Secrets Big", secretCounterBig)
randomCounterBig = Counter(randomlist)
print("Random Big", randomCounterBig)

#Maybe I'm just missing something but they both still seem equally random.
print("They still seem equally random to me.")

#Creating a list to be sorted.
print("Testing sorting methods:")
sortableList = []
sortableList = secretizedList(100, 1, 17)

#Function to sort a list using the insert sort method.
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[i] > key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

#Sorting sortableList using insert sort and timing it
z = 0
while z < 1:
    start = timeit.default_timer()
    insertionSort(sortableList)
    end = timeit.default_timer()
    z += 1
time = end - start
print("Insertion sorting took %.9f seconds." % time)

#Setting sortableList to be random again.
sortableList = secretizedList(100, 1, 17)

#Sorting sortableList with .sort() method.
z = 0
while z < 1:
    start = timeit.default_timer()
    sortableList.sort()
    end = timeit.default_timer()
    z += 1
time = end - start
print("The .sort function took %.9f seconds." % time)

#The sorting methods seem to be pretty equal in time.
print("Both sorting methods seem to be pretty equal in time.")

#Making a sortableList from 1-65535.
print("Now testing sorting methods with a range of 1-65535.")
sortableList = secretizedList(100, 1, 65536)

#Sorting sortableList (1-65535) with insertion sort and timing it.
while z < 1:
    start = timeit.default_timer()
    insertionSort(sortableList)
    end = timeit.default_timer()
    z += 1
time = end - start
print("Insertion sorting took %.9f seconds." % time)

#Making a sortableList from 1-65535.
sortableList = secretizedList(100, 1, 65536)

#Sorting sortableList (1-65535) with .sort() method.
z = 0
while z < 1:
    start = timeit.default_timer()
    sortableList.sort()
    end = timeit.default_timer()
    z += 1
time = end - start
print("The .sort function took %.9f seconds." % time)

#Insertion sort actually seems to be consistently 0.000001 - 0.000005 seconds faster.
print("Insertion sort seems to be consistently 0.000001 - 0.000005 seconds faster.")

#Testing the sorting methods with a list of 500 elements from 1-65535.
print("Now testing sorting methods with a range of 1-65535 and 500 elements.")
sortableList = secretizedList(500, 1, 65536)

#Sorting sortableList (500 elements, 1-65535) with insertion sort and timing it.
while z < 1:
    start = timeit.default_timer()
    insertionSort(sortableList)
    end = timeit.default_timer()
    z += 1
time = end - start
print("Insertion sorting took %.9f seconds." % time)

#Making a sortableList from 1-65535 with 500 elements.
sortableList = secretizedList(500, 1, 65536)

#Sorting sortableList (500 elements, 1-65535) with .sort() method.
z = 0
while z < 1:
    start = timeit.default_timer()
    sortableList.sort()
    end = timeit.default_timer()
    z += 1
time = end - start
print("The .sort function took %.9f seconds." % time)

#The .sort method tends to take 0.00003 - 0.00005 more seconds than the insert method.
print("The .sort method tends to take 0.00003 - 0.00005 more seconds than the insert method. So it might get worse with bigger lists.")
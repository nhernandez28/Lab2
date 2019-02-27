"""
CS2302
Lab2
Purpose: implement several algorithms for finding the median of a list of integers, using objects of the List class
described in class, and compare their running times for various list lengths.
Created on Wed Feb 18, 2019
Olac Fuentes
@author: Nancy Hernandez
"""

import random

# Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev


# List Functions
class List(object):
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None


def Print(L):
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()


def IsEmpty(L):
    return L.head == None


def Append(L, x):
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head

    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next


def Prepend(L, x):
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.head = L.head.next
        L.head = Node(x)


def randomInts(L):
    for i in range(5):
        Append(L, random.randint(1, 31))


def Copy(L):
    return L


def GetLength(L):
    temp = L.head
    count = 0
    while temp is not None:
        count += 1
        temp = temp.next
    return count


def ElementAt(L, n):
    t = L.head
    counter = 0
    while t is not None:
        if counter == n:
            return t.item
        counter = counter + 1
        t = t.next
    return -1


def bubbleSort(L):
    temp = L.head
    swap = True
    while swap:
        current = L.head
        swap = False
        while current.next is not None:
            if current.item > current.next.item:
                temp = current.item
                current.item = current.next.item
                current.next.item = temp
                swap = True
            current = current.next
    return L


def MedianBubble(L):
    C = Copy(L)
    bubbleSort(C)
    median = ElementAt(C, GetLength(C) // 2)
    return median


def mergeSort(L):
    counter = 0
    length = GetLength(L)
    if length < 2:
        return L
    else:
        mid = length // 2
        L1 = List()
        L2 = List()
        temp = L.head
        leftTemp = L1.head
        rightTemp = L2.head
        while temp is not None:
            counter += 1
            if counter <= mid:
                Append(L1, temp.item)
                temp = temp.next
            else:
                Append(L2, temp.item)
                temp = temp.next

        mergeSort(L1)
        mergeSort(L2)

        leftTemp = L1.head
        rightTemp = L2.head
        temp = L.head

        while leftTemp and rightTemp is not None:
            if leftTemp.item < rightTemp.item:
                temp.item = leftTemp.item
                leftTemp = leftTemp.next
                temp = temp.next
            else:
                temp.item = rightTemp.item
                rightTemp = rightTemp.next
                temp = temp.next

        while leftTemp is not None:
            temp.item = leftTemp.item
            leftTemp = temp.next
            temp = temp.next

        while rightTemp is not None:
            temp.item = rightTemp.item
            rightTemp = temp.next
            temp = temp.next
    return L


def MedianMerge(L):
    C = Copy(L)
    mergeSort(C)
    median = ElementAt(C, GetLength(C) // 2)
    return median


def quickSort(L):
    length = GetLength(L)
    if length < 2:
        return L
    elif length > 1:
        pivot = L.head.item
        L1 = List()
        L2 = List()
        current = L.head.next
        while current.next is not None:
            if current.item < pivot:
                current = current.next
            elif current.item >= pivot:

                current = current.next
        quickSort(L1)
        quickSort(L2)

        L.head = L1.head
        L.tail = L2.tail

    return L


def MedianQuickSort(L):
    C = Copy(L)
    quickSort(C)
    median = ElementAt(C, GetLength(C) // 2)
    return median


'''def quickSort2(L):
    length = GetLength(L)
   pivot = 0
   if length < 2:
       return L
   else:
   
   
def MedianQuick2(L):
    C = Copy(L)
    quickSort2(C)
    median = ElementAt(C, GetLength(C) // 2)
    return median'''

L = List()
randomInts(L)
print('Random list is: ')
Print(L)
print()

# BubbleSort
print('List was sorted with bubble sort: ')
print("Median is: ")
print(MedianBubble(L))
Print(L)
print()

# MergeSort
print('List was sorted with merge sort: ')
print("Median is: ")
print(MedianBubble(L))
Print(L)
print()

# QuickSort
print('List was sorted with quick sort: ')
print("Median is: ")
print(MedianQuickSort(L))
Print(L)
print()

# QuickSort2
'''print('List was sorted with quick sort2: ')
print("Median is: ")
print(MedianQuick2(L))
Print(L)
print()'''
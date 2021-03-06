#!/usr/bin/env python
# coding=utf-8


class Item():
    def __init__(self, val, key):
        self.val = val
        self.key = key


    def __eq__(self, other):
        return self.key == other.key


    def __lt__(self, other):
        return self.key < other.key


    def __str__(self):
        return str((self.val, self.key))


def __maxHeapify(heap, i):
    global heapSize

    while True: 
        leftChild = (i << 1) + 1
        rightChild = (i + 1) << 1
        largest = i

        if leftChild < heapSize and heap[leftChild] > heap[largest]:
            largest = leftChild

        if rightChild < heapSize and heap[rightChild] > heap[largest]:
            largest = rightChild

        if largest != i:
            heap[largest], heap[i] = heap[i], heap[largest]
            i = largest
        else:
            break


def __buildMaxHeap(heap):
    for i in range(len(heap) // 2 - 1, -1, -1):
        __maxHeapify(heap, i)


def heapSort(heap):
    global heapSize
    heapSize = len(heap)

    __buildMaxHeap(heap)
    
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapSize -= 1
        __maxHeapify(heap, 0)


if __name__ == '__main__':
    heap = [Item(4, 4), Item(1, 1), Item(3, 3), Item(2, 2), Item(16, 16), Item(9, 9), Item(10, 10), Item(14, 14)]

    heapSort(heap)

    for item in heap:
        print(item.key, end = " ")

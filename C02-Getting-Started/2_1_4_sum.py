#!/usr/bin/env python
# coding=utf-8


def sum(A, B):
    C = []
    j = 0
    
    for i in range(len(A) - 1, -1, -1):
        j = A[i] + B[i] + j
        C.insert(0, j % 2)
        j = j // 2

    C.insert(0, j % 2)
    
    return C


if __name__ == '__main__':
    A = [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
    B = [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]
    C = sum(A, B)
    print('    ', A)
    print('+   ', B)
    print('=', C)

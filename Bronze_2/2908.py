# 2908번 상수

import sys

def input():
    return sys.stdin.readline().rstrip()

num1, num2 = input().split()

num1 = int(num1[::-1])
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else:
    print(num2)
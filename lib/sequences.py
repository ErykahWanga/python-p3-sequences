#!/usr/bin/env python3  

def print_fibonacci(length):
    fibonacci = [0, 1]
    for i in range(2, length):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci[:length]
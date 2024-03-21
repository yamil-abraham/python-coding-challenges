'''
Given a positive integer n. The task is to implement a function factorize(n) which takes this integer as input and returns a list of all its factors in ascending order, excluding 1 and n. 
in ascending order, excluding 1 and n.

The function must return an empty list if the input integer n is less than or equal to 1.

Function signature: def factorize(n: int) -> List[int]:

Input format.

The input consists of a single integer N, for example 12.

Restrictions

The list output will be empty if the number is prime: [].

Output format

The output format must be a list with integers that when dividing the input number also return an integer, except 1 and the number itself. Continuing with the example of 12, the output should be: [2, 3, 4, 6]
'''

from typing import List

def factorize(n: int) -> List[int]:
    divs = []
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            divs.extend([i, n // i]) if i != n // i else divs.append(i)
    return sorted(divs)

N = int(input()) 
if N<=1:
    print([])
else:
    print(factorize(N))
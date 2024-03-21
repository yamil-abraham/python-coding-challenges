'''
Given a list of integers initially containing n elements. Two types of operations need to be performed on this list:

Addition operation: Given an integer x. Insert x at the end of the list. Elimination operation: Given an integer y. Remove the first number y from the list. If y is not present in the list, do nothing. After performing all operations, you need to reverse the order of the items in the list.

The task is to implement a function perform_operations_and_reverse(lst, operations) that takes a list lst and a list of operations tuples. Each tuple of operations represents an operation to be performed on lst. The first element of the tuple represents the type of operation (1 for add, 2 for remove), and the second element represents the value to be added or removed.

The function shall return the inverted list lst after all operations have been performed.

Function signature: def perform_operations_and_reverse(lst: List[int], operations: List[Tuple[int, int]]) -> List[int]:

Input format.

[1, 2, 3],[(1, 4), (2, 2)]

Constraints

N/A

Output format

[4, 3, 1]
'''
from typing import List, Tuple
import sys

def perform_operations_and_reverse(lst: List[int], operations: List[Tuple[int, int]]) -> List[int]:
    for operation_type, value in operations:
        if operation_type == 1:
            lst.append(value)
        elif operation_type == 2:
            if value in lst:
                lst.remove(value)
    lst.reverse()
    return lst

def main():
    input_str = sys.stdin.readline().strip()
    lst, operations = eval(input_str)
    result = perform_operations_and_reverse(lst, operations)
    sys.stdout.write(f"[{', '.join(map(str, result))}]\n")

if __name__ == "__main__":
    main()

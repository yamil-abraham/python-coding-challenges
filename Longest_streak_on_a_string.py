'''
Given a string s containing lowercase alphabetic characters. The task is to implement a function longest_streak(s) that finds the character with the longest streak (the longest substring of repeated characters) in the string and returns a tuple (char, position) where char is the character with the longest streak and position is the starting position of the streak in the original string.

If there are multiple characters with the same longest streak, return the one that appears first in the string.

Function signature: def longest_streak(s: string) -> Tuple[string, int]:

Input format

s = "xxxyyyyyyyyzzzzzzzaaaabbbbbb".

Restrictions

lowercase and uppercase characters are not considered equal.

Output format

The length of the string refers to the number of consecutive occurrences of a character in the string. Thus, in the input example, the output would be ('z', 7)
'''
from typing import List, Tuple
import sys

def longest_streak(s: str) -> Tuple[str, int]:
 max_streak_length = 0
 current_streak_length = 1
 longest_char = s[0]
 longest_char_position = 0
    
 for i in range(1, len(s)):
        if ord(s[i]) == ord(s[i - 1]):
            current_streak_length += 1
        else:
            if current_streak_length > max_streak_length:
                max_streak_length = current_streak_length
                longest_char = s[i - 1]
                longest_char_position = i - current_streak_length
            current_streak_length = 1
    
 if current_streak_length > max_streak_length:
        max_streak_length = current_streak_length
        longest_char = s[-1]
        longest_char_position = len(s) - current_streak_length
    
 return longest_char, longest_char_position
    
def main():
 s = sys.stdin.readline().strip()
 result = longest_streak(s.replace('"', ''))
 sys.stdout.write(f"('{result[0]}', {result[1]})\n")

if __name__ == "__main__":
    main()

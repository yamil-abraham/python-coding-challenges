'''
Given a string s, find the length of the longest substring without repeating characters.

Input Format

Input: s = "abcabcbb"

Constraints

s consists of lowercase English letters

Output Format

Output: 3 Explanation: The longest substring without repeating characters is "abc", which has a length of 3.
'''

def lengthOfLongestSubstring(s):
    char_index = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        char_index[char] = i

        max_length = max(max_length, i - start + 1)

    return max_length

input_str = input()
print(lengthOfLongestSubstring(input_str.split('"')[1]))

# Example usage
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3

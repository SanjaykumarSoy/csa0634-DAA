def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    longest_length = 0
    start = 0

    for index, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = index
        longest_length = max(longest_length, index - start + 1)

    return longest_length
s = "abcabcbb"
output = length_of_longest_substring(s)
print(output)  

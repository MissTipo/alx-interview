from longest_repeated_substring import longestRepeatedSubstring


input_string = "banana"
result = longestRepeatedSubstring(input_string)
if result:
    print(f"The longest repeating non-overlapping substring is: {result}")
else:
    print("No repeating non-overlapping substring found.")
input_string = "aaaaaaaaaaa"
result = longestRepeatedSubstring(input_string)
if result:
    print(f"The longest repeating non-overlapping substring is: {result}")
else:
    print("No repeating non-overlapping substring found.")
input_string = "geeksforgeeks"
result = longestRepeatedSubstring(input_string)
if result:
    print(f"The longest repeating non-overlapping substring is: {result}")
else:
    print("No repeating non-overlapping substring found.")
input_string = "aab"
result = longestRepeatedSubstring(input_string)
if result:
    print(f"The longest repeating non-overlapping substring is: {result}")
else:
    print("No repeating non-overlapping substring found.")
input_string = "aabaabaaba"

result = longestRepeatedSubstring(input_string)
if result:
    print(f"The longest repeating non-overlapping substring is: {result}")
else:
    print("No repeating non-overlapping substring found.")

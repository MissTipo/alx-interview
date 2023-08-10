from longest_substring import longest_substring


input_string = "banana"
result = longest_substring(input_string)
if result:
    print(f"The longest repeating non-overlapping substring is: {result}")
else:
    print("No repeating non-overlapping substring found.")
input_string = "aaaaaaaaaaa"
result = longest_substring(input_string)
if result:
    print(f"The longest repeating non-overlapping substring is: {result}")
else:
    print("No repeating non-overlapping substring found.")
input_string = "geeksforgeeks"
result = longest_substring(input_string)
if result:
    print(f"The longest repeating non-overlapping substring is: {result}")
else:
    print("No repeating non-overlapping substring found.")
input_string = "aab"
result = longest_substring(input_string)
if result:
    print(f"The longest repeating non-overlapping substring is: {result}")
else:
    print("No repeating non-overlapping substring found.")
input_string = "aabaabaaba"

result = longest_substring(input_string)
if result:
    print(f"The longest repeating non-overlapping substring is: {result}")
else:
    print("No repeating non-overlapping substring found.")

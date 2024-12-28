from util import read_input

# Read input using your custom function
input_strings = read_input('../aoc_data/day09.txt')
input_string = ''.join(input_strings)  # Combine all lines into a single string


# Input string
# input_string = "2333133121414131402"

# Initialize the variables
blocks = ""  # For numbers at odd positions (1-based)
spaces = ""  # For numbers at even positions (1-based)

# Loop through the string using 1-based positions
for pos, char in enumerate(input_string, start=1):
    if pos % 2 == 1:  # Odd position (1, 3, 5, ...)
        blocks += char
    else:  # Even position (2, 4, 6, ...)
        spaces += char

# Print the results
#print("Blocks:", blocks)
#print("Spaces:", spaces)

# # Initialize the result variable
# blocks_multi = ""

# # Loop through the string using 0-based indexing
# for index, char in enumerate(blocks):
#     blocks_multi += str(index) * int(char)  # Append the index as many times as the number indicates

# # Print the result
# print("Blocks:", blocks_multi)

# spaces_multi = ""
# for char in spaces:
#     spaces_multi += "." * int(char)  # Append "." as many times as the number indicates

# # Print the result
# print("Spaces:", spaces_multi)

combined_result = ""
# Interleave blocks_multi and spaces_multi
max_length = max(len(blocks), len(spaces))  # Get the max length to avoid index errors
for i in range(max_length):
    # Handle blocks
    if i < len(blocks):
        combined_result += str(i) * int(blocks[i])  # Append the index as many times as the number in blocks

    # Handle spaces
    if i < len(spaces):
        combined_result += "." * int(spaces[i])  # Append "." as many times as the number in spaces

# Print the final combined result
#print("Combined Result:", combined_result)

# Initialize the new combined result and dot residuals
new_combined_result = ""
dot_residuals = ""

# Store the length of the original combined_result for stopping condition
original_length = len(combined_result)

# Process the combined_result string until the total length of results matches the original length
while len(new_combined_result) + len(dot_residuals) < original_length and combined_result:
    char = combined_result[0]  # Take the first character from combined_result
    if char.isdigit():  # If it's a number, add it to the new_combined_result
        new_combined_result += char
    elif char == ".":  # If it's a dot
        # Find the last number in the updated combined_result
        last_number_index = next(
            (i for i in range(len(combined_result) - 1, -1, -1) if combined_result[i].isdigit()),
            None
        )
        if last_number_index is not None:  # If a last number exists
            last_number = combined_result[last_number_index]
            new_combined_result += last_number  # Add it to the result
            # Update combined_result to remove the last number
            combined_result = combined_result[:last_number_index] + combined_result[last_number_index + 1:]
        else:  # If no numbers are left, accumulate the dots
            dot_residuals += char # this is probably not important
            combined_result = combined_result[1:]  # Remove the dot from combined_result
            continue  # Skip to the next iteration
    # Remove the first character after processing
    combined_result = combined_result[1:]

# Print the final corrected results
#print("New Combined Result:", new_combined_result)
# print("Dot Residuals:", dot_residuals) doesnt work, doesnt matter

# Calculate the checksum by multiplying each number with its index and summing them
checksum = sum(int(num) * idx for idx, num in enumerate(new_combined_result))

# Print the calculated checksum
print("Checksum:", checksum)
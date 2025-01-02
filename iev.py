from util import read_input

# Read input using your custom function
input = read_input('./rosalind_data/rosalind_iev.txt')
# input_string = ''.join(input)  # Combine all lines into a single string
# cleaned_string = input.replace(' ', '')
#print(input)

numbers = list(map(int, input[0].split())) # splitting th string into individual parts and making it a list

#print(numbers)

# Define the weights for each genotype pair
weights = [1, 1, 1, 0.75, 0.5, 0]
total = 0

for i in range(len(numbers)):
    total += numbers[i] * weights[i]

# Multiply the total by 2 (for 2 offspring per couple)
result = 2 * total

print(result)
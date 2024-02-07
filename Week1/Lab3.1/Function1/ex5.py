def generate_permutations(s):
    if len(s) <= 1:
        return [s]

    permutations_list = []
    for i in range(len(s)):
        remaining_part = s[:i] + s[i+1:]
        for permutation in generate_permutations(remaining_part):
            permutations_list.append(s[i] + permutation)

    return permutations_list

def print_permutations():
    string_input = input("Enter a string: ")
    all_permutations = generate_permutations(string_input)

    print("All permutations of the string:")
    for permutation in all_permutations:
        print(permutation)

# Call the function
print_permutations()
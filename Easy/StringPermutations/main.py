def get_permutations(input):
	if len(input) == 1:
		yield input
	
	if len(input) == 2:
		yield input[0] + input[1]
		yield input[1] + input[0]
	
	if len(input) > 2:
		for i in range(len(input)):
			first_char = input[i]
			rest_of_string = input[:i] + input[i + 1:]

			for permutation in get_permutations(rest_of_string):
				yield first_char + permutation


if __name__ == "__main__":
	input = "abcd"
	permutations = get_permutations(input)

	for permutation in permutations:
		print(permutation)

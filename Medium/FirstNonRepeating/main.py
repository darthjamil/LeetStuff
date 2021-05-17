from collections import defaultdict

def non_repeating_chars(input):
    charCounts = defaultdict(int)

    for c in input:
        charCounts[c] += 1

    return [c for c in input if charCounts[c] == 1]

if __name__ == '__main__':
    input = "aaaabbbbccccdeeeeefgggghiii"
    non_repeats = non_repeating_chars(input)

    first_non_repeating = non_repeats[0] if len(non_repeats) > 0 else ''
    print(first_non_repeating)

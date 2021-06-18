chars_to_remove = [',', '.', '!', ':', ';', '-', ' ', '?']

def get_longest_palendromes(text):
    if not text: return []
    if len(text) <= 2: return [text]

    palendromes = []

    for window_size in range(len(text), 1, -1):
        num_shifts = len(text) - window_size

        for start_index in range(0, num_shifts + 1):
            end_index = start_index + window_size
            substring = text[start_index:end_index]

            if is_palendrome(substring):
                palendromes.append(substring)

        if len(palendromes) > 0:
            break

    return palendromes


def is_palendrome(text):
    text = _clean(text)
    return _is_palendrome(text)


def _clean(text):
    return ''.join([char for char in text.lower() if char not in chars_to_remove])


def _is_palendrome(text):
    return text and text == text[::-1]


if __name__ == '__main__':
    tests = [
        "", # false
        "lotion", # false
        "racecar", # true
        "Racecar", # true
        "Step on no p ets", # true
        "No lemon no melons", # false
        "Eva - can I see bees in a cave?", # true
        "A man, a plan, a canal: Panama!", # true
        "Aaaaa", # ["Aaaaa"]
        "Babcaaba", # ["aa"] --------> correction, should be ["bab", "aba"]
        "A racecar", # ["racecar"]
        "No lemon no melons", # ["No lemon no melon"] 
    ]

    for test in tests:
        print(f'\nCase: {test}')
        print(f'Cleaned: {_clean(test)}')
        print(f'Is Palendrome: {is_palendrome(test)}')
        print(f'Longest Palendromes: {get_longest_palendromes(test)}')

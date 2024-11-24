def print_unique_elements(array):

    all_elements = set()
    duplicates = set()

    for num in array:
        if num in all_elements:
            duplicates.add(num)
        else:
            all_elements.add(num)

    unique_elements = all_elements - duplicates

    print("Unique elements:", " ".join(map(str, sorted(unique_elements))))


array = [2, 3, 2, 5, 8, 1, 9, 8]
print_unique_elements(array)

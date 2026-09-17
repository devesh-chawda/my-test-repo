def find_duplicates_with_count(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
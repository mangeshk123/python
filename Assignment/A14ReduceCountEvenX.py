from functools import reduce

def main():
    Numbers = [2, 6, 4, 9, 7]

    # Filter: keep only even numbers
    evens = list(filter(lambda x: x % 2 == 0, Numbers))

    # Map: convert each even number to 1 (for counting)
    mapped = list(map(lambda x: 1, evens))

    # Reduce: sum up the mapped values to get count
    count = reduce(lambda a, b: a + b, mapped)

    print("Count of even numbers:", count)

if __name__ == "__main__":
    main()

def containsDuplicate(num_array):
    existing = set()
    for num in num_array:
        if num in existing:
            return True
        existing.add(num)
    return False

def test_case(test_no, num_array):
    print(f"Test Case {test_no}: ", end="")
    print("true" if containsDuplicate(num_array) else "false")

if __name__ == "__main__":
    test_case(1, [1, 2, 3, -1])
    test_case(2, [1, 2, -3, 4])
    test_case(3, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    test_case(4, [0, 0, 0, 1])

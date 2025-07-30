def containsDuplicate(nums):
    existing = set()
    for num in nums:
        if num in existing:
            return True
        existing.add(num)
    return False

if __name__ == "__main__":
    example = [3, 2, 3, 9]
    print("true" if containsDuplicate(example) else "false")

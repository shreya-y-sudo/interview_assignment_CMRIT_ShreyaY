def shift_zeroes(num_array):
    position = 0
    for i in range(len(num_array)):
        if num_array[i] != 0:
            num_array[position], num_array[i] = num_array[i], num_array[position]
            position += 1
    return num_array

def test_case(nums):
    original = nums[:]
    result = shift_zeroes(nums)
    print("Input: ", original)
    print("Output:", result)

test_case([0, 1, 0, 3, 12])
test_case([1, 2, 3, 4])
test_case([0, 0, 0, 0])

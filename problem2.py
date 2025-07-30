def shift_zeroes(num_array):
    position = 0
    for i in range(len(num_array)):
        if num_array[i] != 0:
            num_array[position], num_array[i] = num_array[i], num_array[position]
            position += 1
    return num_array
num_array = [0, 1, 0, 4, 21]
print("Before:", [0, 1, 0, 4, 21])
print("After: ", shift_zeroes(num_array))

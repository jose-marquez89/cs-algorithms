'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # First pass solution
    n = 0
    z = 0

    while arr:
        while arr[z] != 0:
            z += 1
            n = z
            if z >= len(arr) or n >= len(arr):
                return arr
        if arr[n] == 0:
            n += 1
            if z >= len(arr) or n >= len(arr):
                return arr
        else:
            arr[n], arr[z] = arr[z], arr[n]


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    arr = [1, 2, 3, 0, 4, 0, 0]
    # arr = [0, 0, 0, 0, 3, 2, 1]
    # arr = [4,1,2,5]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

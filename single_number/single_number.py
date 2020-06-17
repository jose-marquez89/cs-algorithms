'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # first pass solution
    counts = [0] * (max(arr) + 1)
    for i in arr:
        counts[i] += 1

    for j in range(len(counts)):
        if counts[j] == 1:
            return j
    return None


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

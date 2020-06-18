import time
import logging

FORMAT = "%(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logging.disable(logging.DEBUG)
'''
Input: an integer
Returns: an integer
'''

# old solution
# def eating_cookies(n):
#     if n == 0:
#         return 1
#     upper_list = ['3'] * n
#     upper = int(''.join(upper_list)) + 1
#     valid_ways = []
#     counter = 0
#     logging.debug(f"UPPER: {upper}")
#
#     for i in range(1, upper):
#         nums = [int(x) for x in str(i) if int(x) > 0 and int(x) < 4]
#         if nums in valid_ways:
#             del nums
#             continue
#         logging.debug(f"NUMS {nums}")
#         total = sum(nums)
#         if total == n:
#             counter += 1
#             valid_ways.append(nums)
#             del nums
#
#     return counter


def eating_cookies(n, cache=None):
    # base cases
    if n == 0:
        return 1
    if n < 0:
        return 0
    if not cache:
        cache = {}
    if n in cache:
        return cache[n]
    else:
        value = (eating_cookies(n-1, cache) +
                 eating_cookies(n-2, cache) +
                 eating_cookies(n-3, cache))
        cache[n] = value
        return value


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 17

    start = time.time()
    print(f"There are {eating_cookies(num_cookies)} ways for "
          f"Cookie Monster to eat {num_cookies} cookies")
    end = time.time()
    total_time = end - start
    print("Process executed in %f seconds" % total_time)

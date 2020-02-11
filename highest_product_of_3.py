import unittest
from itertools import combinations
from functools import reduce
import random
import timeit




def highest_product_of_3_toph(list_of_ints):
    # Calculate the highest product of three numbers
    def list_product(items):
        return reduce(lambda x, y: x * y, items)
    if len(list_of_ints) < 3:
        raise Exception("Input list must be three items long")
    elif len(list_of_ints) <= 6:
        candidates = list_of_ints
    else:
        list_sorted = sorted(list_of_ints)
        largest_three = list_sorted[-3:]
        smallest_three = list_sorted[:3]
        candidates = largest_three + smallest_three
    products = []
    for x in combinations(candidates, 3):
        products.append(list_product(x))
    return max(products)







def highest_product_of_3_michael(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception
    first, second = list_of_ints[0], list_of_ints[1]
    min_val, max_val = min(first, second), max(first, second)
    max_two, min_two = first * second, first * second
    max_three, min_three = float('-inf'), float('inf')
    for i in range(2, len(list_of_ints)):
        val = list_of_ints[i]
        max_two_val = max_two * val
        min_two_val = min_two * val
        max_three = max(max_three, max_two_val, min_two_val)
        max_val_val = max_val * val
        min_val_val = min_val * val
        max_two = max(max_two, max_val_val, min_val_val)
        min_two = min(min_two, max_val_val, min_val_val)
        min_val = min(min_val, val)
        max_val = max(max_val, val)
    return max_three



def createList(r1, r2): 
  
    # Testing if range r1 and r2  
    # are equal 
    if (r1 == r2): 
        return r1 
  
    else: 
  
        # Create empty list 
        res = [] 
  
        # loop to append successors to  
        # list until r2 is reached. 
        while(r1 < r2+1 ): 
              
            res.append(r1) 
            r1 += 1
        return res 
      
# Driver Code 
r1, r2 = -1, 1
print(createList(r1, r2)) 


sizes = [x * 10000 for x in range(1, 11)]

list_of_lists = []
for size in sizes:
    list_of_lists.append([random.randint(-100,100) for i in range(size)])

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

runs = []
for size, sublist in zip(sizes, list_of_lists):
    print("Working on {}.".format(size))
    # print(sublist)
    results = {}
    results["size"]: size
    print("Working on Michael.")
    wrapped = wrapper(highest_product_of_3_michael, sublist)
    results["michael"] = timeit.timeit(wrapped, number = 100)
    print("Working on Toph.")
    wrapped = wrapper(highest_product_of_3_toph, sublist)
    results["toph"] = timeit.timeit(wrapped, number = 100)
    print(results)
    runs.append(results)





# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
import unittest


def make_change_no_cache(amount, denominations):
  # print(f'entering make_change with {amount}, {denominations}')
  combos = []
  if all([amount < denom for denom in denominations]):
    return []
  for denom in denominations:
    # print(f'evaluating denom {denom}')
    if denom == amount:
      combos.append([denom])
    elif denom < amount:
      remainder = amount - denom
      for sub_combo in make_change(remainder, denominations):
        # print(sub_combo)
        if len(sub_combo) is not 0:
          this_combo = sorted([denom] + sub_combo)
          # print(this_combo)
          if this_combo not in combos:
            combos.append(this_combo)
    # print(combos)
  return combos


def make_change_yes_cache(amount, denominations, cache):
  # print(f'entering make_change with {amount}, {denominations}')
  if amount in cache.keys():
    return cache[amount]
  combos = []
  if all([amount < denom for denom in denominations]):
    return []
  for denom in denominations:
    # print(f'evaluating denom {denom}')
    if denom == amount:
      combos.append([denom])
    elif denom < amount:
      remainder = amount - denom
      for sub_combo in make_change_yes_cache(remainder, denominations, cache):
        # print(sub_combo)
        if len(sub_combo) is not 0:
          this_combo = sorted([denom] + sub_combo)
          # print(this_combo)
          if this_combo not in combos:
            combos.append(this_combo)
    # print(combos)
  cache[amount] = combos
  return combos


def change_possibilities(amount, denominations):
  
    if amount == 0:
      return 1
  
    if len(denominations) == 0:
      return 0

    denominations = sorted(denominations)

    return len(make_change_yes_cache(amount, denominations, {}))

    # Another possible case: if the amount is smaller than any of the
    # denominations, we could just return zero.

    # Approaches:
    # - Brute force
    # - 

    return 0





# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
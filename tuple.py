from collections import Counter
def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
hex_to_rgb('FFA501')  # (255, 165, 1)

# Converts a hexadecimal color code to a tuple of integers corresponding to its RGB components.

#Use a list comprehension in combination with int() and list slice notation to get the RGB components from the hexadecimal string.
#Use tuple() to convert the resulting list to a tuple.

#######


def digitize(n):
  return list(map(int, str(n)))


digitize(123)  # [1, 2, 3]

# Converts a number to a list of digits.

#Use map() combined with int on the string representation of n and return a list from the result

from collections import Counter



def find_parity_outliers(nums):
  return [
      x for x in nums
      if x % 2 != Counter([n % 2 for n in nums]).most_common()[0][0]
  ]


find_parity_outliers([1, 2, 3, 4, 6])  # [1, 3]

# Finds the items that are parity outliers in a given list.

#Use collections.Counter with a list comprehension to count even and odd values in the list.
#Use collections.Counter.most_common() to get the most common parity.
#Use a list comprehension to find all elements that do not match the most common parity.

#generate a python code for printing index of smallest positive integer. it should only accept a list with positive integers.

def least_positive_index(data):
  """
  This function finds the index of the smallest positive integer in a list.

  Args:
    data: A list of positive integers.

  Returns:
    The index of the smallest positive integer in the list, or -1 if no positive integers are found.
  """
  # Initialize variables
  smallest_positive = None
  smallest_index = -1

  # Loop through the list
  for i, num in enumerate(data):
    # Check if the current number is positive
    if num > 0:
      # If it is, check if it is smaller than the current smallest positive
      if smallest_positive is None or num < smallest_positive:
        smallest_positive = num
        smallest_index = i

  # Return the index of the smallest positive integer
  return smallest_index
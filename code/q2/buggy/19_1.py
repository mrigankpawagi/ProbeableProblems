#write a python program first_positive_integer that takes a string and returns the first positive integer. check for integers including both figuers and words.

import re

def first_positive_integer(text):
  """
  This function finds the first positive integer in a string, including both figures and words.

  Args:
    text: A string containing text and potentially numbers.

  Returns:
    The first positive integer found in the string, or None if no positive integers are found.
  """
  # Combine digits and words representing numbers into a single token
  tokens = re.findall(r"\d+|\w+", text)

  # Find the first positive integer among the tokens
  for token in tokens:
    try:
      number = int(token)
      if number > 0:
        return number
    except ValueError:
      # Ignore non-numeric tokens
      pass

  # No positive integer found
  return None
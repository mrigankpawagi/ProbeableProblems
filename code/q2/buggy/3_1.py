def first_positive_integer(text):
  """
  Finds the first positive integer in a string.

  Args:
    text: A string containing text and possibly an integer.

  Returns:
    The first positive integer found in the string, or None if no positive integers are found.
  """
  for token in text.split():
    try:
      num = int(token)
      if num > 0:
        return num
    except ValueError:
      pass
  return None
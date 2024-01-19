def first_positive_integer(s):
     # Initialize an empty string to store the digits found
    s=s.split(' ')
    for i in s:
       if i.isdigit():
          return(i)
          
    else: return 0
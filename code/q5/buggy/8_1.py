def reorder(data, num):
    try:
        # Validate input types
        if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data) or not isinstance(num, (int, float)):
            raise TypeError("Invalid input types. Please provide a list of numbers and a number.")

        # Handle empty list
        if not data:
            return []

        # Separate numbers smaller than num and larger than num
        smaller_than_num = [x for x in data if x < num]
        larger_than_num = [x for x in data if x >= num]

        # Reorder the list
        reordered_list = smaller_than_num + larger_than_num

        return reordered_list

    except Exception as e:
        return f"Error: {str(e)}"
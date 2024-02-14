def statistics_decorator(func):
    def wrapper(*args, **kwargs):
        # Call the original function
        numbers = func(*args, **kwargs)
        
        # Calculate statistics
        count = len(numbers)
        total = sum(numbers)
        average = total / count
        maximum = max(numbers)
        
        # Print statistics
        print("Numbers read:", numbers)
        print("Count of numbers read:", count)
        print("Average of numbers:", average)
        print("Maximum of numbers:", maximum)
    return wrapper

@statistics_decorator
def printStats(filename):
    numbers_list = []
    with open(filename, 'r') as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))
            numbers_list.extend(numbers)
    return numbers_list

# Example usage:
printStats('numbers.txt')  # Replace 'numbers.txt' with your file name containing numbers

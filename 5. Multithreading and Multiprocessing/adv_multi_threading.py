from concurrent.futures import ThreadPoolExecutor
import time


# Function to simulate work by printing a number
def print_number(number):
    time.sleep(1)  # Simulate some work with a delay
    return f"Processed Number: {number}"


# List of numbers to process
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Start a ThreadPoolExecutor with a maximum of 3 worker threads
# This means at most 3 tasks will run concurrently
with ThreadPoolExecutor(max_workers=3) as executor:
    print("Starting thread pool executor with 3 workers...")
    # Submit tasks to the executor and map the results
    results = executor.map(print_number, numbers)

# Retrieve and print results as they are completed
print("Processing completed. Results:")
for result in results:
    print(result)

# Starting thread pool executor with 3 workers...
# Processing completed. Results:
# Processed Number: 1
# Processed Number: 2
# Processed Number: 3
# Processed Number: 4
# Processed Number: 5
# Processed Number: 6
# Processed Number: 7
# Processed Number: 8
# Processed Number: 9
# Processed Number: 10

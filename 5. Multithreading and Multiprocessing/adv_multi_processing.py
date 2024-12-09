from concurrent.futures import ProcessPoolExecutor
import time


# Function to simulate a time-consuming task (computational workload)
def square_number(number):
    time.sleep(2)  # Simulate computation delay
    return f"Square: {number * number}"  # Return square of the number


# List of numbers to process
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 2, 3, 12, 14]

# Multiprocessing logic (spawn worker processes for each task)
if __name__ == "__main__":
    print("Starting multiprocessing with ProcessPoolExecutor...")

    # Using ProcessPoolExecutor with a maximum of 3 worker processes
    with ProcessPoolExecutor(max_workers=3) as executor:
        # Map the computation function to numbers - each number is processed by a worker process
        results = executor.map(square_number, numbers)

    # Process and print results as they are returned by worker processes
    print("Processing results from worker processes:")
    for result in results:
        print(result)

    print("Multiprocessing execution completed.")

# Main Process Check (if __name__ == "__main__":)
# This ensures that the multiprocessing context is only executed on the main process. It's a safeguard against issues on platforms like Windows.

# Starting multiprocessing with ProcessPoolExecutor...
# Processing results from worker processes:
# Square: 1
# Square: 4
# Square: 9
# Square: 16
# Square: 25
# Square: 36
# Square: 49
# Square: 64
# Square: 81
# Square: 121
# Square: 4
# Square: 9
# Square: 144
# Square: 196
# Multiprocessing execution completed.

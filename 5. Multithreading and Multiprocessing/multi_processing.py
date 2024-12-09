import multiprocessing
import time


# Function to calculate and print the square of numbers
def square_numbers():
    for i in range(5):
        time.sleep(1)  # Simulate a time-consuming computation
        print(f"Square: {i*i}")


# Function to calculate and print the cube of numbers
def cube_numbers():
    for i in range(5):
        time.sleep(1.5)  # Simulate a slightly longer computation
        print(f"Cube: {i*i*i}")


# The main block to ensure processes are created and managed correctly
if __name__ == "__main__":
    # Create two processes, each executing a separate function
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    # Record the start time for performance measurement
    start_time = time.time()

    # Start both processes
    print("Starting processes...")
    p1.start()
    p2.start()

    # Wait for both processes to complete before moving forward
    p1.join()
    p2.join()

    # Calculate and print the total time taken
    elapsed_time = time.time() - start_time
    print(f"Total execution time: {elapsed_time:.2f} seconds")

# Starting processes...
# Square: 0
# Cube: 0
# Square: 1
# Cube: 1
# Square: 4
# Cube: 8
# Square: 9
# Cube: 27
# Square: 16
# Cube: 64
# Total execution time: 7.50 seconds

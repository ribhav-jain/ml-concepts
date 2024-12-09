import threading
import time


# Function to simulate a task that prints numbers with a delay
def print_numbers():
    for i in range(5):
        time.sleep(2)  # Simulate a time-consuming task
        print(f"Number: {i}")


# Function to simulate a task that prints letters with a delay
def print_letters():
    for letter in "abcde":
        time.sleep(2)  # Simulate a time-consuming task
        print(f"Letter: {letter}")


# Create two threads, each targeting a specific function
t1 = threading.Thread(target=print_numbers, name="NumberThread")
t2 = threading.Thread(target=print_letters, name="LetterThread")

# Record the start time
start_time = time.time()

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish execution
t1.join()
t2.join()

# Calculate and print the total time taken
elapsed_time = time.time() - start_time
print(
    f"Total execution time: {elapsed_time:.2f} seconds"
)  # Total execution time: 10.00 seconds

import multiprocessing
import time


# Simulate a CPU-bound computation, such as factorial calculation
def compute_factorial(number):
    print(f"Computing factorial for {number}")
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(f"Factorial of {number} is {result}")
    return result


# List of numbers to compute factorial for
numbers = [100, 150, 200, 250, 300]


if __name__ == "__main__":
    start_time = time.time()

    # Use ProcessPoolExecutor to parallelize computation
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print("Results computed:", results)
    print(
        f"Total execution time using multiprocessing: {end_time - start_time} seconds"
    )

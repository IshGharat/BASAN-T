import time

def delay(seconds):
    def decorator(func):
        last_execution_time = 0

        def wrapper(*args, **kwargs):
            nonlocal last_execution_time
            current_time = time.time()

            if current_time - last_execution_time >= seconds:
                result = func(*args, **kwargs)
                last_execution_time = current_time
                return result
            else:
                print(f"Function '{func.__name__}' is on cooldown. Try again later.")

        return wrapper

    return decorator

# Usage:
# @delay(5)  # Allow the function to be called every 5 seconds
# def my_function():
#     print("Function executed")

# # Example usage:
# while True:
#     my_function()
#     time.sleep(1)  # Call the function once per second

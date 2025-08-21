# Create @retry(times=3) that re-invokes the wrapped function if it raises Exception.

from functools import wraps

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count = 0
            while count < times:
                try:
                    result = func(*args, **kwargs)
                    count += 1
                    print("Successful")
                    return result
                except Exception as e:
                    if count < times - 1:
                        count += 1
                        continue
                    else:                        
                        print("Unsuccessful execution")
                        raise e 
        return wrapper
    return decorator

call_count = 0

@retry(times=3)
def test(n):
    global call_count
    call_count += 1
    print(f"Attempt #{call_count} with n={n}")
    if call_count < 3:
        raise ConnectionError("Network temporarily unavailable")
    return f"Success! Result: {n * 2}"

test(3)
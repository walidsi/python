def log_with_name(operation):
    def log_result(func):
        def inner(*args, **kwargs):
            result = func(*args)
            print(operation, result)
            return result
        return inner
    return log_result

@log_with_name('add')
def add(a, b):
    return a + b

@log_with_name('subtract')
def subtract(a, b):
    return a - b

def main():
    add(5,3)
    subtract(5,3)

if __name__ == "__main__":
    main()

import time
def time_cal(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(end-start)
    return wrapper



@time_cal
def calculate_10000():
    total = sum(range(10000))
    print(total)
    print("done")

calculate_10000()
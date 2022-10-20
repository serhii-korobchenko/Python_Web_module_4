import concurrent.futures
from random import randint
from time import sleep


def calculate_some(name):
    print(f"start {name}")
    sleep(randint(0, 3))
    print(f"{name} finished")
    return randint(0, 10)


arguments = (
    "Bill",
    "Jill",
    "Till",
    "Sam",
    "Tom",
    "John",
)

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(calculate_some, arguments))

print(results)
import pathlib
from tqdm import tqdm
import time
from faker import Faker
import arrow
import pyinputplus as pyip
from icecream import ic
from tenacity import retry, stop_after_attempt
import random
from rich.progress import track


this_directory = pathlib.Path(__file__).parent
print(f"This directory: {this_directory}")

this_directory.as_uri()
print(f"Directory as URI: {this_directory.as_uri()}")

this_directory.drive
print(f"Drive: {this_directory.drive}")

this_directory.home()
print(f"Home directory: {this_directory.home()}")

this_directory.is_file()
print(f"Is file: {this_directory.is_file()}")
this_directory.is_dir()
print(f"Is directory: {this_directory.is_dir()}")

for parent in tqdm(this_directory.parents):
    time.sleep(1)  # Simulate some processing time

fake = Faker()
for _ in range(3):
    print(fake.name())
    print(fake.address())
    print(fake.email())
    print(fake.company())
    print(fake.job())
    print(fake.phone_number())
    print("---")

now = arrow.now()
print(f"Current time: {now}")
print(f"Formatted time: {now.format('YYYY-MM-DD HH:mm:ss')}")
now_plus_5 = now.shift(hours=+5)
print(f"Time plus 5 hours: {now_plus_5.format('YYYY-MM-DD HH:mm:ss')}")

#age = pyip.inputInt("Enter your age: ", min=1)
#print(f"You are {age} years old.")

x = 42
ic(x * 2)

random.seed(42)

@retry(stop=stop_after_attempt(10))
def flaky_task():
    """A task that may fail randomly."""
    if random.random() < 0.7:
        print("Attempt failed, retrying...")
        raise Exception("Failed!")
    return "Success!"

print(flaky_task())

for parent in track(this_directory.parents):
    time.sleep(1)  # Simulate some processing time

import argparse

# Initialize ArgumentParser
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("name", type=str, help="Your name")  # Positional argument
parser.add_argument("-age", type=int, default=25, help="Your age (optional)")  # Optional argument

# Parse arguments
args = parser.parse_args()

# Use parsed values
print(f"Hello, {args.name}! You are {args.age} years old.")
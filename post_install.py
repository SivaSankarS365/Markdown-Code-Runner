import os
import subprocess
import sys

def check_dependency(command, name):
    try:
        subprocess.check_call([command, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{name} is installed.")
    except subprocess.CalledProcessError:
        print(f"Warning: {name} is not installed.")
    except FileNotFoundError:
        print(f"Warning: {name} is not found in the system path.")

def main():
    # Check for g++
    check_dependency('g++', 'g++')

    # Check for python3
    check_dependency('python3', 'python3')

    # Additional instructions for the user to update config.py
    print("\nIf you encounter issues, ensure that the paths for python3 and g++ are correctly set in config.py.")

if __name__ == "__main__":
    main()

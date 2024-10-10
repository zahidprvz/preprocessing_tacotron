import os
import re

# Path to the folder containing text files
folder_path = "/Users/macbook/Desktop/cleaned_data/text"  # Update this path with your actual path

# Change directory to the folder_path
os.chdir(folder_path)

# Function to extract the number from the filename
def get_file_number(file_name):
    match = re.search(r'(\d+)', file_name)  # Find the numeric part
    return int(match.group(1)) if match else None

# List all .txt files
txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

# Sort the files based on the numeric value in their names
txt_files.sort(key=get_file_number)

# Loop through the sorted list and rename files to 1.txt, 2.txt, etc.
for index, file_name in enumerate(txt_files, start=1):
    new_file_name = f"{index}.txt"
    os.rename(file_name, new_file_name)
    print(f"Renamed {file_name} to {new_file_name}")

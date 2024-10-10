import os

# Path to the folder containing files
folder_path = "/Users/macbook/Desktop/voice"  # Update this path with your actual path

# Change to the directory
os.chdir(folder_path)

# Loop through all files in the directory and delete .txt files
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        os.remove(file_name)
        print(f"Deleted {file_name}")

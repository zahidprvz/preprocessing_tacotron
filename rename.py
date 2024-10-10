import os
import re

# Path to the folder containing audio files
folder_path = "/Users/macbook/Desktop/cleaned_data/audio"  # Update this path with your actual path

# Change directory to the folder_path
os.chdir(folder_path)

# Function to extract the number from the filename
def get_file_number(file_name):
    match = re.search(r'(\d+)', file_name)  # Find the numeric part
    return int(match.group(1)) if match else None

# List all .wav files
wav_files = [f for f in os.listdir(folder_path) if f.endswith(".wav")]

# Sort the files based on the numeric value in their names
wav_files.sort(key=get_file_number)

# Loop through the sorted list and rename files to 1.wav, 2.wav, etc.
for index, file_name in enumerate(wav_files, start=1):
    new_file_name = f"{index}.wav"
    os.rename(file_name, new_file_name)
    print(f"Renamed {file_name} to {new_file_name}")

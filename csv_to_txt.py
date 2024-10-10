import csv
import os

# Input CSV file path (the CSV file with your original data)
csv_input_file = "/Users/macbook/Desktop/cleaned_data/metadata.csv"  # Update this with your actual file path

# Output TXT file path (the file to save the updated format)
txt_output_file = "/Users/macbook/Desktop/cleaned_data/list.txt"  # Update this with your desired output file path

# Base path for the updated file format
base_path = "/content/TTS-TT2/wavs/"

def update_csv_format(input_csv, output_txt, base_path):
    rows = []  # To store rows temporarily
    file_count = 0  # To keep track of the number of rows processed

    # Read the CSV file
    with open(input_csv, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='|')

        # Iterate through rows
        for row in reader:
            # Extract the audio file name and transcription
            audio_file = row[0].strip()
            transcription = row[1].strip()

            # Extract the number from the audio file name (e.g., audio_1.wav -> 1)
            audio_number = int(audio_file.split('_')[-1].split('.')[0])

            # Append a period (.) at the end of the transcription if it's not already present
            if not transcription.endswith('.'):
                transcription += '.'

            # Store the rows in a list (audio_number, new_path, transcription)
            new_audio_path = f"{base_path}{audio_number}.wav"
            rows.append((audio_number, new_audio_path, transcription))

            file_count += 1

            # Break the loop after 72 rows to match the limit
            if file_count == 72:
                break

    # Sort the rows based on the audio file number in ascending order
    rows.sort(key=lambda x: x[0])

    # Write the sorted rows to the TXT file
    with open(output_txt, mode='w', encoding='utf-8') as outfile:
        for row in rows:
            outfile.write(f"{row[1]}|{row[2]}\n")
            print(f"Updated: {row[1]} -> {row[2]}")

    print(f"TXT file has been updated, sorted, and saved to {output_txt}")

# Call the function to update the CSV format, sort by file number, and store the output in TXT format
update_csv_format(csv_input_file, txt_output_file, base_path)

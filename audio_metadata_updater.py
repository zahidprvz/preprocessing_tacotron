import os
import shutil
import taglib

def update_metadata(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(1, 73):  # Adjust to the number of files in your folder + 1
        input_file = os.path.join(input_folder, f"{i}.wav")
        output_file = os.path.join(output_folder, f"{i}.wav")

        if os.path.exists(input_file):
            # Load WAV file and update metadata
            with taglib.File(input_file) as audio:
                # Set the title to match the file name without the extension
                audio.tags["TITLE"] = [f"{i}"]
                # Set the track number to match the file name without the extension
                audio.tags["TRACKNUMBER"] = [f"{i}"]

                # Save updated WAV file
                audio.save()

            # Copy the updated file to the output folder instead of moving it
            shutil.copy2(input_file, output_file)

            print(f"Updated metadata for {i}.wav: title='{i}', track number={i}")
        else:
            print(f"File {i}.wav not found.")


if __name__ == "__main__":
    # Make sure to use absolute paths starting with "/" for Unix-based systems (like macOS)
    input_folder = "/Users/macbook/Desktop/cleaned_data/audio"  # Correct absolute path
    output_folder = "/Users/macbook/Desktop/cleaned_data/audio1"  # Correct absolute path
    update_metadata(input_folder, output_folder)

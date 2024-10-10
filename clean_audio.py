import os
import subprocess

# Define paths
folder_path = "Users/macbook/Desktop/transcriptions"  # Path to the folder containing your .wav audio files
output_folder = "Users/macbook/Desktop/cleaned_voice"  # Folder to store cleaned audio files

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Function to run FFmpeg commands
def run_ffmpeg(input_file, output_file, command):
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Processed {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {input_file}: {e}")


# Loop through all .wav files in the folder
for audio_file in os.listdir(folder_path):
    if audio_file.endswith('.wav'):
        input_path = os.path.join(folder_path, audio_file)

        # Step 1: Remove silence from audio
        cleaned_audio_path = os.path.join(output_folder, f"cleaned_{audio_file}")
        remove_silence_command = f"ffmpeg -i \"{input_path}\" -af silenceremove=1:0:-50dB \"{cleaned_audio_path}\""
        run_ffmpeg(input_path, cleaned_audio_path, remove_silence_command)

        # Step 2: Normalize volume of the cleaned audio
        normalized_audio_path = os.path.join(output_folder, f"normalized_{audio_file}")
        normalize_volume_command = f"ffmpeg -i \"{cleaned_audio_path}\" -af \"volume=1.5\" \"{normalized_audio_path}\""
        run_ffmpeg(cleaned_audio_path, normalized_audio_path, normalize_volume_command)

        # Step 3: Reduce background noise
        final_audio_path = os.path.join(output_folder, f"final_{audio_file}")
        noise_reduction_command = f"ffmpeg -i \"{normalized_audio_path}\" -af \"afftdn\" \"{final_audio_path}\""
        run_ffmpeg(normalized_audio_path, final_audio_path, noise_reduction_command)

        print(f"Final cleaned file for {audio_file} saved as {final_audio_path}")

print("Audio cleaning process completed.")

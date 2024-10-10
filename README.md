# Tacotron2 Training

This repository contains the implementation for training the Tacotron2 model for text-to-speech synthesis. Tacotron2 is an end-to-end speech synthesis system that converts text to mel spectrograms, which can then be converted to audio using a vocoder.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Training](#training)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- End-to-end text-to-speech synthesis.
- Support for multi-GPU training with PyTorch's distributed training capabilities.
- Option for half-precision training (FP16) for faster training times.
- Logging and validation capabilities using TensorBoard.

## Requirements

- Python 3.6 or higher
- PyTorch 1.0.0 or higher
- NumPy
- [Apex](https://github.com/NVIDIA/apex) (for FP16 training)
- Other dependencies listed in `requirements.txt`

## Getting Started

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/zahidprvz/preprocessing_tacotron.git
   cd preprocessing_tacotron
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Install NVIDIA Apex (if using FP16):
   ```bash
   git clone https://github.com/NVIDIA/apex
   cd apex
   pip install -v --editable ./
   ```

### Configuration

Configuration is managed via a hyperparameters JSON file. You can define various parameters such as learning rate, batch size, and training files.

Example of a hyperparameters file (`hparams.json`):
```json
{
  "learning_rate": 0.001,
  "batch_size": 32,
  "epochs": 1000,
  "training_files": "path/to/training_data.txt",
  "validation_files": "path/to/validation_data.txt",
  "fp16_run": false,
  "distributed_run": false,
  "ignore_layers": []
}
```

### Training

To start training the Tacotron2 model, you can use the provided `train.py` script. The command can be structured as follows:

```bash
python train.py -o output_directory -l log_directory --hparams_file hparams.json --n_gpus <number_of_gpus>
```

#### Command-Line Arguments

- `-o`, `--output_directory`: Directory to save checkpoints.
- `-l`, `--log_directory`: Directory to save TensorBoard logs.
- `-c`, `--checkpoint_path`: Path to a checkpoint to resume training (if any).
- `--warm_start`: Flag to load model weights only and ignore specified layers.
- `--n_gpus`: Number of GPUs to use for training.
- `--rank`: Rank of the current GPU in distributed training.
- `--group_name`: Distributed group name.
- `--hparams`: Comma-separated name=value pairs for hyperparameters.
- `--hparams_file`: Path to a hyperparameters JSON file.

## Usage

After training, you can use the trained model for text-to-speech synthesis by implementing a separate script or function to convert text to audio using the generated mel spectrograms and a vocoder (such as WaveGlow or HiFi-GAN).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions or bug reports.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Key Sections Explained:

1. **Introduction**: A brief overview of what the project does.
2. **Features**: Highlights the main functionalities of your implementation.
3. **Requirements**: Lists the necessary dependencies for running the project.
4. **Getting Started**: Guides users on how to set up the project.
5. **Configuration**: Provides examples of configuration files.
6. **Training**: Instructions on how to initiate training.
7. **Usage**: Briefly describes how to use the trained model.
8. **Contributing**: Invites contributions to the project.
9. **License**: States the licensing for the project.

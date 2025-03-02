# Audio Analysis and Visualization Tool

## Overview
This project provides tools for visualizing and analyzing audio waveforms and their frequency content using Python. It leverages **NumPy**, **Matplotlib**, and **SciPy** to plot waveforms and perform Fourier Transforms on WAV audio files.

## Features
- **Waveform Visualization**: Plots the time-domain representation of an audio file.
- **Fourier Transform Analysis**: Computes and visualizes the frequency components of an audio file.
- **Automatic Stereo-to-Mono Conversion**: If an audio file is stereo, it automatically converts it to mono for analysis.

## Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install numpy matplotlib scipy
```

## Usage
### Running the Script
The main script allows users to visualize audio waveforms and frequency spectra. Run it using:
```bash
python main.py path/to/audio.wav --fourier waveform
```

### Command-Line Arguments
- `audio_file` (required): Path to the WAV audio file.
- `--fourier` (optional): Choose between `waveform` (default) and `fourier`.
  
#### Example Usage
1. **Plot Waveform:**
   ```bash
   python main.py example.wav --fourier waveform
   ```
2. **Plot Fourier Transform:**
   ```bash
   python main.py example.wav --fourier fourier
   ```

## File Structure
```
.
├── main.py          # Main script for audio visualization
├── side-by-side.py  # Additional utility script
├── LICENSE.md       # License file
├── .gitignore       # Git ignore file
```

## License
This project is licensed under the terms specified in the `LICENSE.md` file.

## Contribution
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.


import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import argparse
import os
from scipy.fftpack import fft

def plot_waveform_and_fourier(audio_file, show_fourier=False):
    # Read audio file
    sample_rate, data = wav.read(audio_file)
    
    # Check if stereo and convert to mono if needed
    if len(data.shape) > 1:
        data = data.mean(axis=1)
    
    # Generate time axis for waveform
    time = np.linspace(0, len(data) / sample_rate, num=len(data))
    
    # Compute Fourier Transform if needed
    if show_fourier:
        N = len(data)
        freq_data = fft(data)
        freq_bins = np.linspace(0, sample_rate, N)

        # Create a single figure with two subplots (side by side)
        fig, axes = plt.subplots(1, 2, figsize=(14, 4))

        # Plot waveform on the left
        axes[0].plot(time, data, label="Waveform", color='blue')
        axes[0].set_xlabel("Time (seconds)")
        axes[0].set_ylabel("Amplitude")
        axes[0].set_title("Audio Waveform")
        axes[0].legend()
        axes[0].grid()

        # Plot Fourier Transform on the right
        axes[1].plot(freq_bins[:N // 2], np.abs(freq_data[:N // 2]), label="Magnitude Spectrum", color='red')
        axes[1].set_xlabel("Frequency (Hz)")
        axes[1].set_ylabel("Magnitude")
        axes[1].set_title("Fourier Transform Representation")
        axes[1].legend()
        axes[1].grid()

        # Adjust layout and show the plots
        plt.tight_layout()
        plt.show()
    
    else:
        # If not showing Fourier, just plot the waveform
        plt.figure(figsize=(10, 4))
        plt.plot(time, data, label="Waveform", color='blue')
        plt.xlabel("Time (seconds)")
        plt.ylabel("Amplitude")
        plt.title("Audio Waveform")
        plt.legend()
        plt.grid()
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="Plot waveform and Fourier transform of an audio file.")
    parser.add_argument("audio_file", type=str, help="Path to the audio file (WAV format).")
    parser.add_argument("--fourier", action="store_true", help="Display Fourier Transform representation.")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.audio_file):
        print("Error: File not found.")
        return
    
    plot_waveform_and_fourier(args.audio_file, show_fourier=args.fourier)

if __name__ == "__main__":
    main()
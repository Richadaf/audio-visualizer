import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import argparse
import os
from scipy.fftpack import fft


def plot_waveform(audio_file):
    # Read audio file
    sample_rate, data = wav.read(audio_file)
    
    # Check if stereo and convert to mono if needed
    if len(data.shape) > 1:
        data = data.mean(axis=1)
    
    # Generate time axis
    time = np.linspace(0, len(data) / sample_rate, num=len(data))
    
    # Plot waveform
    plt.figure(figsize=(10, 4))
    plt.plot(time, data, label="Waveform", color='blue')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Audio Waveform")
    plt.legend()
    plt.grid()
    plt.show()


def plot_fourier_transform(audio_file):
    # Read audio file
    sample_rate, data = wav.read(audio_file)
    
    # Check if stereo and convert to mono if needed
    if len(data.shape) > 1:
        data = data.mean(axis=1)
    
    # Compute Fourier Transform
    N = len(data)
    freq_data = fft(data)
    freq_bins = np.linspace(0, sample_rate, N)
    
    # Plot Fourier Transform (Magnitude Spectrum)
    plt.figure(figsize=(10, 4))
    plt.plot(freq_bins[:N // 2], np.abs(freq_data[:N // 2]), label="Magnitude Spectrum", color='red')
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("Fourier Transform Representation")
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
    
    plot_waveform(args.audio_file)
    
    if args.fourier:
        plot_fourier_transform(args.audio_file)


if __name__ == "__main__":
    main()

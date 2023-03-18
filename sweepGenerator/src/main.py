import tkinter as tk
import numpy as np
import soundfile as sf
from scipy import signal

def Sweep(sampleRate:int, duration, waveformType) ->list:
    """
    This function takes 3 inputs and returns a sine, square or triangle sweep samples.
    """
    totalSamples = sampleRate * duration
    time = np.linspace(0, duration, totalSamples, False)
    startFreq = 20
    stopFreq = 10000
    if waveformType == "Sine" or waveformType == "sine" :
        sweepFreqs = np.linspace(startFreq, stopFreq, totalSamples)
        sweepSignal = np.sin(2 * np.pi * sweepFreqs * time)
    elif waveformType == "Square" or waveformType == "square":
        sweepFreqs = np.linspace(startFreq, stopFreq, totalSamples)
        duty_cycle = 0.5
        sweepSignal = signal.square(2 * np.pi * sweepFreqs * time, duty=duty_cycle)
    elif waveformType == "Triangle" or waveformType == "triangle":
        sweepFreqs = np.linspace(startFreq, stopFreq, totalSamples)
        sweepSignal = signal.sawtooth(2 * np.pi * sweepFreqs * time, width=0.5)
    else:
        raise ValueError("Invalid waveform type. Choose Sine, Square or Triangle.")
    return sweepSignal

def generate_signal():
    sample_rate = int(sample_rate_entry.get())
    duration = int(duration_entry.get())
    waveform_type = waveform_type_var.get()
    signal = Sweep(sample_rate, duration, waveform_type)
    file_name = file_name_entry.get()
    sf.write(file_name, signal, sample_rate)

root = tk.Tk()
root.geometry("250x150")
root.title("Sweep Generator")

sample_rate_label = tk.Label(root, text="Sample Rate:")
sample_rate_label.grid(row=0, column=0)
sample_rate_entry = tk.Entry(root)
sample_rate_entry.grid(row=0, column=1)

duration_label = tk.Label(root, text="Duration (s):")
duration_label.grid(row=1, column=0)
duration_entry = tk.Entry(root)
duration_entry.grid(row=1, column=1)

waveform_type_label = tk.Label(root, text="Waveform Type:")
waveform_type_label.grid(row=2, column=0)
waveform_type_var = tk.StringVar()
waveform_type_var.set("sine")
waveform_type_menu = tk.OptionMenu(root, waveform_type_var, "sine", "square", "triangle")
waveform_type_menu.grid(row=2, column=1)

file_name_label = tk.Label(root, text="File Name:")
file_name_label.grid(row=3, column=0)
file_name_entry = tk.Entry(root)
file_name_entry.grid(row=3, column=1)

generate_button = tk.Button(root, text="Generate Signal", command=generate_signal)
generate_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
import matplotlib.pyplot as plt
import numpy
import librosa, librosa.display
y, sr = librosa.load('Simple-drum-loop-116-bpm.wav') 
beat_times = librosa.beat.beat_track(x, sr=sr, start_bpm=120, units='time')
onset_env = librosa.onset.onset_strength(y, sr=sr,aggregate=np.median)


hop_length = 512
plt.figure(figsize=(8, 4))
times = librosa.frames_to_time(np.arange(len(onset_env)),sr=sr, hop_length=hop_length)
plt.plot(times, librosa.util.normalize(onset_env),label='Onset strength')
plt.vlines(times[beat_times], 0, 1, alpha=0.5, color='r',linestyle='--', label='Beats')
plt.legend(frameon=True, framealpha=0.75)# Limit the plot to a 15-second window
plt.xlim(15, 30)
plt.gca().xaxis.set_major_formatter(librosa.display.TimeFormatter())
plt.tight_layout()

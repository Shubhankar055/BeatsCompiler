import librosa, librosa.display # Returns array of timestamps of beat
def beat_dect(audio):
    lst = []
    x, sr = librosa.load(audio)
    ipd.Audio(x, rate=sr)
    tempo, beat_times = librosa.beat.beat_track(x, sr=sr, start_bpm=120, units='time')
    

    x = beat_times
    return(x)

import sounddevice as sd
import soundfile as sf
import time

def sync_record(fileName, duration, fs, channels):
    print('Recording started ..')
    myRecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(fileName, myRecording, fs)
    print('Recoding is done')

sync_record('../../data/ivanu_gelaya.wav', 15, 16000, 1)
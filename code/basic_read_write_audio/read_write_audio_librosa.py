import librosa
y, sr = librosa.load('../../data/sample_test_file.wav')
librosa.output.write_wav('../../data/basic_read_write/new_librosa_audio.wav', y, sr)
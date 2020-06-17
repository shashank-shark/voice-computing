from scipy.io import wavfile
fs, data = wavfile.read('../../data/sample_test_file.wav')
wavfile.write('../../data/basic_read_write/scipy_gen_audio_file.wav', fs, data)

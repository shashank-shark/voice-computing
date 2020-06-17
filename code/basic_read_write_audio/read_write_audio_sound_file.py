import soundfile as sf
data, fs = sf.read('../../data/sample_test_file.wav')
sf.write('../../data/basic_read_write/soundfile_gen_audio.wav', data, fs)
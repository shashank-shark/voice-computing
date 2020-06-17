from pydub import AudioSegment
data = AudioSegment.from_wav('../../data/sample_test_file.wav')
data.export('../data/new_file.wav')
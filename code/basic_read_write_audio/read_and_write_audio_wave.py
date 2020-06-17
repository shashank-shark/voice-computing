import wave

data = wave.open('../../data/sample_test_file.wav')
parmas = data.getparams()
print(parmas)
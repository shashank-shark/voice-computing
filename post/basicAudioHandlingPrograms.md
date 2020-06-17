# Sample read and write operation of audio file with different libraries
## **pydub** read / write audio file
```python
from pydub import AudioSegment
data = AudioSegment.from_wav('../../data/sample_test_file.wav')
data.export('../data/new_file.wav')
```

## **scipy** read / write audio file
```python
from scipy.io import wavfile
fs, data = wavfile.read('../../data/sample_test_file.wav')
wavfile.write('../../data/basic_read_write/scipy_gen_audio_file.wav', fs, data)
```

## **wave** read and print params of audio file
```python
import wave
data = wave.open('../../data/sample_test_file.wav')
parmas = data.getparams()
print(parmas)
```

## **librosa** read / write audio file
```python
import librosa
y, sr = librosa.load('../../data/sample_test_file.wav')
librosa.output.write_wav('../../data/basic_read_write/new_librosa_audio.wav', y, sr)
```

## **soundfile** read / write an audio file
```python
import soundfile as sf
data, fs = sf.read('../../data/sample_test_file.wav')
sf.write('../../data/basic_read_write/soundfile_gen_audio.wav', data, fs)
```

# Sample audio file manipulation programs with **sox** linux program
## **sox** reverse an audio file
```python
import os
os.system('sox ../../data/sample_test_file.wav ../../data/reverse_file.wav reverse')
```

## **sox** double the volume for an audio file
```python
import os
os.system('sox -v 2.0 ../../data/sample_test_file.wav ../../data/doubleSound.wav')
```

## **sox** decrease the volume by half of the audio file
```python
import os
os.system('sox  -v -0.5 ../../data/sample_test_file.wav ../../data/halfDecreasedVolume.wav')
```

## **sox** convert stereo to mono
```python
import os
os.system('sox ../../data/sample_test_file.wav -c 1 ../../data/mono.wav')
```

## **sox** convert mono to stereo
```python
import os
os.system('sox ../../data/sample_test_file.wav -c 2 ../../data/stereo.wav')
```

## **sox** increase the speed of play
```python
import os
os.system('sox ../../data/sample_test_file.wav ../../data/double_the_speed.wav speed 2.0')
```

## **sox** change the sample rate
```python
import os
os.system('sox ../../data/sample_test_file.wav -r 16000  ../../data/16000hz.wav')
```

## **sox** convert to 16bit audio quality
```python
import os
os.system('sox -b 16 ../../data/sample_test_file.wav ../../data/16bitwav.wav')
```
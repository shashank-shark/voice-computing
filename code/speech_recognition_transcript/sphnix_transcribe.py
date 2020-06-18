import speech_recognition as sr_audio
import sounddevice as sd
import soundfile as sf
import os, json, datetime

def sync_record(fileName, duration, fs, channels):
    print('Recording started')
    myRecording =  sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(fileName, myRecording, fs)
    print('Recording done')

def transcribe_audio_by_sphnix(fileName):
    r = sr_audio.Recognizer()

    with sr_audio.AudioFile(fileName) as source:
        audio = r.record(source)

    text = r.recognize_sphinx(audio)
    print('Transcript : ' + text)
    return text

def store_transcript(fileName, transcript):
    jsonFileName = fileName[0:-4] + '.json'
    print ('Saving %s to current directory'%(jsonFileName))
    data = {
        'date' : str(datetime.datetime.now()),
        'fileName': fileName,
        'transcript': transcript
    }
    print(data)
    jsonFile = open(jsonFileName, 'w')
    json.dump(data, jsonFile)
    jsonFile.close()

# load the necessary auth file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/shashank/gcp credentials/voice-computing-project-d7d167a8bba1.json'

fileName = 'sync_record.wav'
sync_record(fileName, 10, 16000, 1)
transcript = transcribe_audio_by_sphnix(fileName)

# now write the transacript into a .json file
store_transcript(fileName, transcript)
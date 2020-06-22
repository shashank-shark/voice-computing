# Creating a custom text to speech bot
Here we will be creating a custom text to speech bot using ```pyttsx3``` python module. At the end we will be generating a customized `default_voice.json` which contains our custom spearking rate, voices etc. as shown below.

```json
{
	"rate": 175,
	"rates": [175, 150, 125, 100, 200, 225, 250, 275, 300],
	"voiceid": "armenian",
	"voiceids": ["bulgarian", "default", "english", "english_wmids", "english-us", "persian", "armenian", "armenian-west"]
}
```

## ```text_to_speech_custom.py```
```python
import json
import pyttsx3
import time
import os
import random

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak_text_custom(text, voiceid, rate):
    start = time.time()
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voiceid)
    engine.say(text)
    engine.runAndWait()
    end = time.time()

    return end - start

def select_speed():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    likes = list()

    speak_text('I Will go a bit slower now. Let me know what you think!')
    slower_rates = [rate-25, rate-50, rate-75, rate-100]

    for i in range(len(slower_rates)):
        new_rate = slower_rates[i]
        engine.setProperty('rate', new_rate)
        engine.say('The Quick brown fox jumped over the lazy dog')
        engine.runAndWait()
        like = input ('Did you like this voice speed rate (%s) ? yes or no'%(str(new_rate)))
        if like not in ['y', 'yes', 'n', 'no']:
            like = input('input not recognized. Did you like this voice yes or no ?')
        likes.append(new_rate)

    # set back to normal speed to tell the user to speed up
    engine.setProperty('rate', rate)
    speak_text('I will now speak a bit faster. Let me know that do you think')
    faster_rates = [rate, rate+25, rate+50, rate+75, rate+100]

    for i in range(len(faster_rates)):
        new_rate = faster_rates[i]
        engine.setProperty('rate', new_rate)
        engine.say('The Quick brown fox jumped over the lazy dog')
        engine.runAndWait()
        like = input('Did you like this voice speed rate (%s) ? yes or no' % (str(new_rate)))
        if like not in ['y', 'yes', 'n', 'no']:
            like = input('input not recognized. Did you like this voice yes or no ?')
        likes.append(new_rate)

    return likes

def select_voice(rate):
    text = 'The Quick brown fox jumped over the lazy dog'
    likes = list()

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for voice in voices:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.setProperty('voice', voice.id)
        engine.say(text)
        engine.runAndWait()

        like = input('Did you like this voice yes or no : %s ?'%(str(voice.id)))
        if like not in ['y', 'yes', 'n', 'no']:
            like = input('input not recognized. Did you like this voice yes or no ?')
        if like in ['y', 'yes']:
            likes.append(voice.id)

    return likes

def rand_select(rand_list):
    randint = random.randint(0, len(rand_list) - 1)
    return rand_list[randint]


# implement these functions to select a voice and rate that you like
if 'default_voice.json' not in os.listdir():
    speak_text('I will now adjust my speaking rate')
    rates = select_speed()
    rate = rand_select(rates)
    speak_text('I will now let you select a new voice')
    voiceids = select_voice(rates)
    voiceid = rand_select(voiceids)

    # now save these variables as default_voice.json file
    jsonFile = open('default_voice.json', 'w')
    data = {
        'rate': rate,
        'rates': rates,
        'voiceid': voiceid,
        'voiceids': voiceids
    }
    json.dump(data, jsonFile)
    jsonFile.close()
else:
    default_voice = json.load(open('default_voice.json'))
    voiceid = default_voice['voiceid']
    rate = default_voice['rate']

text = input('type the text that you want to speak. \n')

spoken_time = speak_text_custom(text, voiceid, rate)
print('it took %s seconds to speak this text'%(str(spoken_time)))
```
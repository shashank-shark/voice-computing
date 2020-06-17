from pydub import AudioSegment
song = AudioSegment.from_wav('../../data/sample_test_file.wav')

# get the first 10 seconds and pydub uses milliseconds as its unit
ten_seconds = 10 * 1000
first_10_seconds = song[:ten_seconds]
last_five_seconds = song[-5000:]

# make beginning louder and end quiter
# we try to increase the beginning by 6dB and decrease the sound of ending by 3dB
beginning = first_10_seconds + 6
ending = last_five_seconds - 3

# combine the segments
without_the_middle = beginning + ending

# 1.5 second crossfade
with_style = beginning.append(ending, crossfade=1500)

# repeat the clip twice
do_it_over = with_style * 2

awesome = do_it_over.fade_in(2000).fade_out(3000)
awesome.export("../../data/mashup.mp3", format="mp3")
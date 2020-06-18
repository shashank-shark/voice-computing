import sounddevice as sd

mics = sd.query_devices()
default_devices = sd.default.device
default_input = default_devices[0]
default_output = default_devices[1]

# set the default input device
sd.default.device = 0

for i in range(len(mics)):
    print(mics[i])

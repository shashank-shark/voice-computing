## Setting the development environment
1. Installing and setting up the python virtual environment.
2. Installing the necessary python modules.

### 1. Installing and setting up the python virtual environment.
We use the following commands to setup `virtualenv` on our linux operating system.<br>
$ `sudo apt update`<br>
$ `sudo apt upgrade`<br>
$ `sudo apt install python3-virtualenv`
<br><br>
Now we create a new python3 virtual enviroment named `voice-comp`.<br>
$ `virtualenv voice-comp`<br>

Activate the virtual voice-comp environment.<br>
$ `source voice-comp/bin/activate`

### 2. Installing necessary python modules
| module name  |  command |
|---|---|
| pydub  | `pip install pydub`  |
|  wave |  `pip install wave` |
| librosa  | `pip install librosa`  |
| scipy | `pip install scipy` |
| soundfile | `pip install soundfile` |
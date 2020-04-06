###############################################
#
# Created by - Jatan Vyas
#
# Code to convert Speech commands to ID,
# and then perform a fixed operation.
#
# Speech settings - from model files
#
###############################################

# Import statements
from fuzzywuzzy import process
from pocketsphinx import LiveSpeech
from os import system
from tkinter import Tk, Label, Button, Radiobutton, IntVar

flag = True
retcode = -1                        # Default retcode

commands = [
    'hello',                 # ID - 0				                # Define commands for string matching
    'bye',                   # 1
    'normal view',           # 2
    'three d view',          # 3
    'terminal',              # 4
    'file explorer',         # 5
]

speech = LiveSpeech(                                                # Speech object for PS
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm='en_in\en_in.cd_cont_5000',
    lm='en_in\en-us.lm.bin',
    dic='en_in\custom.dic')

print("Speech model loaded")

# Create GUI app
app = Tk()
app.title("Voice Controlled GUI")
app.geometry("600x400")

v = IntVar()
v.set(1)

txt = Label(app, text="Welcome!", font="24")
rb1 = Radiobutton(app, text="Normal view", variable=v, value=1)
rb2 = Radiobutton(app, text="3D view", variable=v, value=2)
txt.pack(pady=20)
rb1.pack(pady=20)
rb2.pack(pady=20)

# app.mainloop()                                                # Not required since we'll be updating GUI manually

print("GUI ready, entering loop")
for phrase in speech:  # Speech recognized in chunks
    print(phrase)
    if phrase is not None:  # Audio is detected
        spoken = process.extractOne(str(phrase), commands)
        print(spoken)
        if int(spoken[1]) > 50:                                 # Confidence > 50 by fuzzywuzzy
            retcode = commands.index(spoken[0])
            if retcode == 0 and flag:                           # Flag for current state
                flag = False                                    # start program

            elif retcode == 1:
                app.destroy()
                break

            elif retcode == 2:
                v.set(1)

            elif retcode == 3:
                v.set(2)

            elif retcode == 4:
                system('cmd.exe')

            elif retcode == 5:
                system('explorer')

            else:
                print("Can't recognize")
            app.update()

        else:
            print("low confidence, no command sent")
            retcode = -1                                        # Low confidence, return -1
        print("retcode: " + str(retcode))

app.quit()
print("Exiting...")

# Voice-controlled GUI using Pocketsphinx

For more details, please visit the blogs at [my website](http://jatanvyas.me/pocketsphinx-home-page).

### 1. About

This Python script creates a GUI that can be controlled using speech commands. There are some obvious flaws but the purpose of this snippet is to demonstrate how such a program can be written.

Current script executes a few basic commands as mentioned below, and uses a tweaked pre-trained Indian English model. For more details on how to get started with Pocketsphinx, visit [here](http://jatanvyas.me/pocketsphinx-home-page/interfacing-pocketsphinx-python). 

### 2. Installation

a. This version is build on Python 3.7 running on Windows. OS specific commands will have to updated if running on Linux/Mac.

b. Considering you have Python 3.7 with _pip_ installed, get the rest of the required modules using 

`
pip install -r requirements.txt
`

c. Execute the script - the GUI should be displayed on saying "hello".

### 3. Speech Commands

Currently, the script supports the following commands -

- "hello" to open up the GUI

- "Normal view", for selecting a radio button of the same name

- "3D view", for selecting a radio button of the same name

- "terminal", to open the command prompt.

- "file explorer" to open the Windows File Explorer. 

### 4. Customization

To add more commands, follow these steps - 

a. Add the required words in the **en_in/custom.dic** file. You can get the pronunciation from the complete _en_in.dic_ file, available [here](https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Indian%20English/).

b. Update the _commands_ python list (line 21 of the script).

That's it! 

### 5. Troubleshooting

- You'll have to make minor changes for running on Python 2.7

- Installing Pocketsphinx on Windows requires SWIG. See complete instructions [here](http://jatanvyas.me/pocketsphinx-home-page/interfacing-pocketsphinx-python).

- Check that microphone is connected to the system to receive audio. Also check the volume - too low or too high will result in poor accuracy.


-----


Hope this helps you and inspires you to create something better. Good luck!
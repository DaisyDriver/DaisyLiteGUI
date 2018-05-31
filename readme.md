# **DaisyLiteGUI**
### A graphical user interface to the DaisyDriver open-hardware microscope controller.
#### Features
+ Motor control - natural mapped buttons provide tactile interface to the motors
+ Preview feed - see where you are on the sample
+ Sizes adapted for the official Raspberry Pi touch screen

Current version: 1.0

*Documentation in progress.*

#### Requirements
+ Raspberry Pi 3B or 3B+ with the latest version of Raspbian Stretch installed
+ PiCamera v2
+ DaisyDriver

#### Installation
1. Open terminal window and navigate to the directory you want to install DaisyLiteGUI
2. Enter the command `git clone https://github.com/OpenDaisy-Microscopy/DaisyLiteGUI.git`
3. Once this has finished, navigate into the DaisyLiteGUI folder using `cd DaisyLiteGUI`
4. Then run the install script to ensure all required dependencies are installed `bash install.sh`
5. Now, to open DaisyLiteGUI use the command `python3 DaisyLiteGUI.py`
6. When opening DaisyLiteGUI subsequently, you will need to navigate to this directory again and run the command in step 5.

#### To do
+ Improve error handling
+ Add support for multiple cameras
+ Refactor code for clarity and readability
+ Write camera test on load up which uses raspistill to take (and then deletes) a test picture
+ Investigate a more robust way of determining serial port (currently just hard-coded)

#### Contributions
Feel free to open an issue or send a pull request.

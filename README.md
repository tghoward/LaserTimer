# LaserTimer
Laser timer code for Raspberry Pi (Python) for Science Olympiad car competitions

This is set up to run on a Raspberry Pi wired to two photosensors. The first
sensor begins timing, the second ends timing. The sensors take three wires,
3.3 V (red), ground (black), and signal via pins 18 and 23 (yellow wires in my phone lines). 

Laser lights span the track and trigger the photosensors. 

Steps:
1. plug RPi into power or computer to power it up
2. Connect ssh into RPi - via ethernet cable or other approach (ssh pi@zebra3.local)
3. set up sensors and lasers, connect wires to plugs in RPi. 
4. run the python script. (python compTimer2.py)

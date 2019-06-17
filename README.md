# CopterMove
A python script to move a Bebop 2 drone. Uses the PathPlanning library to avoid obstacles

## System Overview
![System overview](/Figures/Copter%20Move.jpg)

## Installation

Requires:
 - Python 3.6
 - pip
 - python venv
 
 1) Create a python virtual environment somewhere in your documents. Run the Instructions below *_OR_* follow this guide https://docs.python.org/3/tutorial/venv.html
 
    a) Run this command `python3 -m venv venvName` to create a python3 virtual environment.
    
    b) Run this command `cd venvName` to move into the virtual environement.

    c) Run this command `source bin/activate` to source the virtual environment's python installation. Your terminal should now show your `venvName` before each line.
    
 2) Install the requried pip packages. Run the Instructions below *_OR_* follow this guide https://pyparrot.readthedocs.io/en/latest/installation.html

    a) Run this command `which pip`. Make sure the output points to a file that is in your venv.
    
    b) Run this command `pip install untangle zeroconf pyparrot` to install the required packages.
    
 3) Install the path-planning (kholysa) package along with matplotlib 

    a) Run this command `pip install matplotlib path-planning-kholysa` to install the required packages for path planning.
    
## Running
Run the `EntryPoint.py` script with your python interpreter. Make sure you connect to a drone (simulated or real). Make sure you have enough physical space for real drones.

### Physical Drones

Make sure your device has a wifi network adapter and can connet to the drone's wifi network

### Virtual Drones
 
IP address should be specified when connecting to a virtual drone. Look at the Sphinx-Parrot software for how to start a simulated drone
- `bebop = Bebop(ip_address="10.202.0.1")`
This simulation is considered a SITL (Software in the Loop). Parrot does not currently support HITL (Hardware in the Loop)

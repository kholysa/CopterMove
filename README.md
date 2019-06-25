# CopterMove
A python script to move a Bebop 2 drone. Uses the PathPlanning library to avoid obstacles

## System Overview
![System overview](/Figures/Copter%20Move.jpg)

## Installation

Requires:
 - Python 3.6
 - pip
 - python venv

### Linux and MacOS environments
 1) Create a python virtual environment somewhere in your documents. Run the Instructions below *_OR_* follow this guide https://docs.python.org/3/tutorial/venv.html
 
    a) Run this command `python3 -m venv venvName` to create a python3 virtual environment.
    
    b) Run this command `cd venvName` to move into the virtual environement.

    c) Run this command `source bin/activate` to source the virtual environment's python installation. Your terminal should now show your `venvName` before each line.
    
 2) Install the requried pip packages. Run the Instructions below *_OR_* follow this guide https://pyparrot.readthedocs.io/en/latest/installation.html

    a) Run this command `which pip`. Make sure the output points to a file that is in your venv.
    
    b) Run this command `pip install untangle zeroconf pyparrot` to install the required packages.
    
 3) Install the path-planning (kholysa) package along with matplotlib 

    a) Run this command `pip install matplotlib path-planning-kholysa` to install the required packages for path planning.

### Windows

 1) Create a python virtual environment somewhere in your documents. Run the Instructions below *_OR_* follow this guide https://docs.python.org/3/tutorial/venv.html
 
    a) Run this command `pip install virtualenv` to install the virtualenv tool.
    
    b) Run this command `virtualenv myenv` to create a virtual environment.

    c) Run this command `myenv\Scripts\activate` to source the virtual environment's python installation. Your terminal should now show your `myenv` before each line.
    
 2) Install the requried pip packages. Run the Instructions below *_OR_* follow this guide https://pyparrot.readthedocs.io/en/latest/installation.html

    a) Run this command `which pip`. Make sure the output points to a file that is in your venv.
    
    b) Run this command `pip install untangle zeroconf pyparrot` to install the required packages.
    
 3) Install the path-planning (kholysa) package along with matplotlib 

    a) Run this command `pip install matplotlib path-planning-kholysa` to install the required packages for path planning.

## Running
Run the `EntryPoint.py` script with your python interpreter. Make sure you connect to a drone (simulated or real). Make sure you have enough physical space for real drones.

### Paramters
All units are in SI Standard Units (meters, seconds...)

- Start: Starting Position of the copter. Must be an integer number * step size away from the Goal.
e.g. Start = (6.3, 8.1) Step Size = 0.5, Goal = (9.8,2.6) Goal _*CANNOT*_ be something like (9.9,2.3)

- Goal: Goal of the copter. Must be an integer number * step size away from the Start

- Barriers: Location of obstacles in the universe

- Universe Size: Smallest discrete area in the universe

- Drone Step Size: Smallest discrete movement by the copter

- Risk Factor: Multiplier that affects the size of the barrier (1 will not affect the barrier sizes, 2 will double their length and width)

### Physical Drones

Make sure your device has a wifi network adapter and can connet to the drone's wifi network

### Virtual Drones
 
IP address should be specified when connecting to a virtual drone. Install Sphinx-Parrot from the commands below *_OR_* look at the Sphinx-Parrot online documentation for how to install and start a simulated drone

#### Sphinx Installation

Requires:
 - Linux Ubuntu 18.04
 
1- Run these commands in a terminal
 a) echo "deb http://plf.parrot.com/sphinx/binary `lsb_release -cs`/" | sudo tee /etc/apt/sources.list.d/sphinx.list > /dev/null
 b) sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 508B1AE5
 c) sudo apt-get update
 d) sudo apt-get install parrot-sphinx
 
2- If all goes well, you should be able to start sphinx with a bebop drone
 a) sudo systemctl start firmwared.service
 b) sphinx /opt/parrot-sphinx/usr/share/sphinx/drones/bebop2.drone

Troubleshooting:
- You may run into an issue where you can't start sphinx without the `sudo` command. *FIND FIX LINK*
- Depending on your ubuntu distibution, you may need to run `sudo apt-get install libatomic1`

- `bebop = Bebop(ip_address="10.202.0.1")`
This simulation is considered a SITL (Software in the Loop). Parrot does not currently support HITL (Hardware in the Loop)

# Eye Socket - A Pupil-Labs Recorder Socket

This is a simple python class that handles all communications with Pupil-Labs trackers through the ZMQ library. Nothing fancy here, just a more convenient copy of pupil labs' own helper script and my previous implementation, [pupil_middleman](https://github.com/mtaung/pupil_middleman). 

The tool is built for internal use at our labs, but feel free to modify and distribute as you wish.

## Installation

## Dependencies

* This package was made for ```pupil capture 1.14.9```; Using newer versions of pupil may very well break, and we have precedence to believe that caution should be exercised.
* The tool was built in python 3, specifically for use with psychopy 3.4; You may find varying success or convenience using this in other python environments.
* You will need ```ZMQ``` and ```msgpack``` to communicate with pupil capture and to to use notifications. This can be accomplished with the ```requirements.txt``` file in this package via:
~~~
pip install -r requirements.txt
~~~

### Setup & Import

This repository is prepared as a package that you can easily install using pip:

~~~ 
pip install git+https://github.com/mtaung/pupil_socket.git 
~~~

You will notice that ```__init__.py``` in ```pupil_socket``` automatically imports the ZMQsocket class. This is because I prefer to access the class directly. You may want to change this before installing into your environment. 

## Use

The class handles the initialisation of the ZMQ socket. The address for this will default to localhost:50020, as these are the defaults for pupil-labs systems.

```connect()```: Connect to the defined ZMQ socket. Run this after initialising the socket object in your experiment.

```start_calibration()``` If you want to calibrate, it may be better to calibrate within a recording, depending on your desired workflow. This way, you can recalibrate offline if required.

```stop_calibration()```: Stops the pupil calibration procedure. This shouldn't be necessary if the calibration is completed properly.

```start_recording()```: Starts a pupil recording. You can optionally input a directory name into the parameter ```dir_name```, which will rename the master directory of any recordings under this title.

```stop_recording()```: Stops a recording when specified. You will want to run this to ensure that your recorded data have complete headers.

```set_time()```: Sets the time on the pupil trackers. By default, pupil clock is not fixed. We presently synchronise our clocks manually at the start of a recording session and align data post-hoc; I personally find this more informative in my work. For those that need consistent realtime sync, I am looking to implement Pupil-Labs' own time sync functionality in the future.

```notify()```: This functionality is currently incomplete and requires some further work to get going. If you're interested in this or have done so before, feel free to submit a PR.

## TODO

* Validate a generic notify() function
* Implement previously used middleman functionality i.e. pure py sockets for interfacing with tools that do not utilise ZMQ. 
* Implement time sync appropriately

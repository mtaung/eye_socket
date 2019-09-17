# Eye Socket - A Pupil-Labs Recorder Socket

This is a simple python class that handles all communications with Pupil-Labs trackers through the ZMQ library. Nothing fancy here, just a more convenient copy of pupil labs' own helper script and my previous implementation, [pupil_middleman](https://github.com/mtaung/pupil_middleman). 

The tool is built for internal use at our labs, but feel free to modify and distribute as you wish.

## Installation

### Dependencies

* This package was made for ```pupil capture 1.14.9```; Using newer versions of pupil may very well break, and we have precedence to believe that caution should be exercised.
* The tool was built in python 3, specifically for use with psychopy 3.4; You may find varying success or convenience using this in other python environments.
* You will need ZMQ to communicate with pupil capture.
* You will need msgpack to use notifications.

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

```start_recordign()```: Starts a pupil recording. You can optionally input a directory name into the parameter ```dir_name```, which will rename the master directory of any recordings under this title.

```stop_recording()```: Stops a recording when specified. You will want to run this to ensure that your recorded data have complete headers.

```set_time()```: Sets the time on the pupil trackers. By default, pupil trackers will use UNIX epoch timestamps. You can leave it as is and normalise them after the fact; I personally find this more informative in my work.  

```notify()```: This is the way pupil handles 'triggers'. Note that I haven't tested this particular method yet, so it likely breaks. It would generally be better protocol to record any internal data for your experiment through psychopy rather than pupil. I use this when working with stimulus that do not have convenient native means to generate data.

## TODO

* Validate notify()
* Implement previously used middleman functionality i.e. pure py sockets for interfacing with tools that do not utilise ZMQ. 

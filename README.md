# rpi.burnin
This library provides an interface from the Rasperberry Pi GPIO to burn-in
related actvitities.

## Acknowledgement
* `alarm`: Preliminary fire alarm detection by Yipeng Sun.
    Further improvements made by Jorge Ramirez.
* `mux`: Preliminary voltage read-out from prototype mux boards is implemented
  by Rohan Rajagopalan.

* `therm`: multisensor.py is a script that reads the output files made by the ds18b20 thermometers and runs a multithreaded process with each thread dedicated to reading and outputting the data values from one thermometer.
    Written by Jorge Ramirez, improvements from Yipeng Sun.
* `moist`: leaksensor.py is a script that uses the LS2600 leak sensor in order to monitor for leaks. If the LS2600 has both contacts in water, then the script will record this and track for how long in the variable 'leak counter'. Otherwise, the script does nothing. more info at the bottom of the .py file. 
    Written by Jorge Ramirez, improvements from Yipeng Sun.

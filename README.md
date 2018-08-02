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
* `moist`: leaksensor.py is a script that activates an alarm when the LS-2600 Leak Sensor has detected a leak. **Note:** for the LS-2600 to work, both of its contacts must be submerged in the same pool of water.
    Written by Jorge Ramirez, improvements from Yipeng Sun.

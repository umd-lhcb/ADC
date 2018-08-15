# rpi.burnin
This library provides an interface from the Rasperberry Pi GPIO to burn-in
related actvitities.

## `therm`
`multisensor.py` is a script that reads the output files made by the ds18b20
thermometers and runs a multithreaded process with each thread dedicated to
reading and outputting the data values from one thermometer. **To set a delay
on recording, run script in terminal with an integer to specify the delay in
seconds:**
```
python thermsensor.py 4
```
will have a 4 second delay between each round of recording.

Written by Jorge Ramirez, improvements by Yipeng Sun.

## `moist`
`leaksensor.py` is a script that uses the LS2600 leak sensor in order to monitor
for leaks. If the LS2600 has both contacts in water, the sensor will close the
circuit and then the script will sense the High and track for how long in the
variable 'leak counter'.

Written by Jorge Ramirez, improvements by Yipeng Sun.

## `alarm`
Preliminary fire alarm detection by Yipeng Sun. Further improvements made by
Jorge Ramirez.

## `mux`
Preliminary voltage read-out from prototype mux boards is implemented by Rohan
Rajagopalan.

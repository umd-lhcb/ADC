from pathlib import Path


def detect_sensors():
     # Detect how many sensors there are
    sensor_dir = "/sys/bus/w1/devices/"  # expected location of sensors
    scandir = Path(sensor_dir)  # set directory to be scanned
    sensorfolders = []  # save sensor folders in here

    for item in scandir.iterdir():
        if item.is_dir() and str(item.stem)[:8] == '28-00000':
            sensorfolders.append(item)

    return sensorfolders

def give_sensor_path(index):
    #print(detect_sensors()[index])
    return detect_sensors()[index]

def give_sensor_serial(index):
    print(str(detect_sensors()[index].stem)[8:])


def list_all_sensors():
    for item in range(len(detect_sensors())):
        print(give_sensor_serial(item))

give_sensor_path(2)
give_sensor_serial(2)
print()
list_all_sensors()
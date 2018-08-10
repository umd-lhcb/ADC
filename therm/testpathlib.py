from pathlib import Path

sensorfolders = []  # save sensor folders in here

def detect_sensors():
     # Detect how many sensors there are
    sensor_dir = "/sys/bus/w1/devices/"  # expected location of sensors
    scandir = Path(sensor_dir)  # set directory to be scanned

    for item in scandir.iterdir():
        if item.is_dir() and str(item.stem)[:8] == '28-00000':
            sensorfolders.append(item)
            print('appended')

    return sensorfolders


def give_sensor_path(index):
    return sensorfolders[index]


def give_sensor_serial(index):
    return str(detect_sensors()[index].stem)[8:]


def list_all_sensors():
    for x in range(len(detect_sensors())):
        print((give_sensor_serial(x)))

detect_sensors()
print(sensorfolders[1])
print(give_sensor_path(4))
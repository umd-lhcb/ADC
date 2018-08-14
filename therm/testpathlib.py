from pathlib import Path

sensorfolders = []  # save sensor folders in here


def detect_sensors():
     # Detect how many sensors there are
    sensor_dir = "/sys/bus/w1/devices/"  # expected location of sensors
    scandir = Path(sensor_dir)  # set directory to be scanned
    print('\nDetecting sensors and adding to list...')
    for item in scandir.iterdir():
        if item.is_dir() and str(item.stem)[:8] == '28-00000':
            sensorfolders.append(item)
            print('sensor ' + str(item.stem)[8:] + ' appended.\n')
    return sensorfolders


def give_sensor_path(index):
    return sensorfolders[index]


def give_sensor_serial(index):
    return str(sensorfolders[index].stem)[8:]


def list_all_sensors():
    print(str(len(sensorfolders)) + ' sensors found:')
    for item in range(len(sensorfolders)):
        print((give_sensor_serial(item)))


detect_sensors()

list_all_sensors()
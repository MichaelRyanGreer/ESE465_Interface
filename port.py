import sys
import glob
import serial

##### CODE AUTHOR: THOMAS KELLY ################################################
##### https://github.com/WURacing/TelemetryWeb/blob/master/serial_ports.py #####

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def get_port():
    ports = serial_ports()
    if (ports != []):
        print("The following serial ports are available:")
        print(ports)
        port = input("Please enter the XBee radio port:")
        if port in ports:
            return port
        else:
            print("-- Port not recognized, please try again --")
            return get_port()
    else:
        print("No serial ports found")
        sys.exit()

##############################################################################

def write_atten(address, value):

	if (address > 12 or address < 0):
		return -1

	address = (address & 0x000F) << 16

	value = (value * 65535) & 0x00FF

	write = 0b1010 | address | value

	port.write(write)

	return 0

def close():

	port.close()

	return 0

port = serial.Serial(get_port(), 9600)

if (port.isOpen()):
	port.close()

port.open();



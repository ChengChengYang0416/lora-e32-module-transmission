import serial

# set serial port and baudrate
port = '/dev/ttyUSB0'
baudrate = 115200
ser = serial.Serial(port, baudrate)
print("connected to: " + ser.portstr)

while True:
	try:
		# read data from serial port and decode
		data = ser.readline().decode('utf-8')
		print(data)
	except Exception as error_messages:
		# exception
		print(error_messages)
		break

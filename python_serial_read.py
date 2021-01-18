import serial

# set serial port and baudrate
port = '/dev/ttyUSB0'
baudrate = 115200
ser = serial.Serial(port, baudrate)
print("connected to: " + ser.portstr)
counter = 0

while True:
	try:
		# read data from serial port and decode
		data = ser.readline().decode('utf-8')
		global counter
		counter += 1
		if data == 'end\n':
			print("End of the transmission test.\n")
			print(repr(counter-3) + " packages received.\n")
			counter = 0
		else:
			print(data)
	except Exception as error_messages:
		# exception
		print(error_messages)
		break

from ymodem.Socket import ModemSocket
import serial

serial_io = serial.Serial(port='COM18',baudrate=115200)

# define read
def read(size, timeout = 3):
    serial_io.timeout = timeout
    return serial_io.read(size)

# define write
def write(data, timeout = 3):
    serial_io.write_timeout = timeout
    serial_io.write(data)
    serial_io.flush()
    return

# create socket
cli = ModemSocket(read, write)

# send multi files
#cli.send(['./411APP_quick.bin'])

cli.send(['./411APP.bin'])


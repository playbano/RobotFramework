from pymodbus.client.serial import ModbusSerialClient
import time

# Serial port settings
serial_port = 'COM5'  # Update with your serial port
baudrate = 9600
parity = 'N'
stopbits = 1
bytesize = 8

# Modbus slave address
slave_address = 1  # Update with the address of your MODBUS slave device

# Create a Modbus serial client
client = ModbusSerialClient(
    method='rtu',
    port=serial_port,
    baudrate=baudrate,
    parity=parity,
    stopbits=stopbits,
    bytesize=bytesize,
    timeout=1  # Adjust timeout as needed
)

# Open the serial port connection
if not client.connect():
    print("Failed to connect to Modbus RTU over serial.")
    exit(1)

try:
    while True:
        # Example: Write to a holding register (address=0, value=12345)
        register_address = 0  # Holding register address
        register_value = 12345  # Value to write

        # Send write request
        result = client.write_register(register_address, register_value, unit=slave_address)

        if not result.isError():
            print(f"Write successful: Holding register {register_address} set to {register_value}.")
        else:
            print(f"Error writing to holding register: {result}")
        time.sleep(1)

finally:
    # Close the serial port connection
    client.close()

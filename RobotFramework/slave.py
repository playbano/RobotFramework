from pymodbus.client.serial import ModbusSerialClient
import time

# Serial port settings
serial_port = 'COM6'  # Update with your serial port (e.g., 'COM1' on Windows)
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
    print(f"Failed to connect to Modbus RTU over serial port {serial_port}.")
    exit(1)

try:
    # Infinite loop to continuously read data from the MODBUS slave
    while True:
        # Example: Read holding registers (address=0, count=5)
        register_address = 0  # Starting address of the holding registers to read
        count = 5  # Number of holding registers to read

        # Send read request
        result = client.read_holding_registers(register_address, count, unit=slave_address)

        if not result.isError():
            # Print the read data
            print(f"Read successful: Holding registers {register_address} to {register_address + count - 1}: {result.registers}")
        else:
            print(f"Error reading holding registers: {result}")

        # Add a delay (optional) before next read
        time.sleep(1)  # Sleep for 1 second before next read

except KeyboardInterrupt:
    # Handle KeyboardInterrupt (Ctrl+C) to gracefully exit the loop
    print("\nLoop interrupted by user.")

finally:
    # Close the serial port connection
    client.close()
    print("Serial port connection closed.")

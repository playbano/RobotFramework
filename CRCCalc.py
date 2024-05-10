def modbusCrc(msg:str) -> int:
    crc = 0xFFFF
    for n in range(len(msg)):
        crc ^= msg[n]
        for i in range(8):
            if crc & 1:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc


data = '020400340001'

msg = bytes.fromhex(data)
crc = modbusCrc(msg)
print("0x%04X"%(crc))            

ba = crc.to_bytes(2, byteorder='little')
print(data+"%02x%02x"%(ba[0], ba[1]))




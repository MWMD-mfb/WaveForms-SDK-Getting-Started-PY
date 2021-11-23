def write(device_handle, data, cs):
    """
        send data through SPI

        parameters: - device handle
                    - data of type string, int, or list of characters/integers
                    - chip select line number
    """
    # cast data
    if type(data) == int:
        data = "".join(chr(data))
    elif type(data) == list:
        data = "".join(chr(element) for element in data)

    # enable the chip select line
    dwf.FDwfDigitalSpiSelect(device_handle, ctypes.c_int(cs), ctypes.c_int(0))

    # create buffer to write
    data = bytes(data, "utf-8")
    buffer = (ctypes.c_ubyte * len(data))()
    for index in range(0, len(buffer)):
        buffer[index] = ctypes.c_ubyte(data[index])

    # write array of 8 bit elements
    dwf.FDwfDigitalSpiWrite(device_handle, ctypes.c_int(1), ctypes.c_int(8), buffer, ctypes.c_int(len(buffer)))

    # disable the chip select line
    dwf.FDwfDigitalSpiSelect(device_handle, ctypes.c_int(cs), ctypes.c_int(1))

    return

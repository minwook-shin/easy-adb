def send_command(device, command):
    response = device.shell(command)
    return response

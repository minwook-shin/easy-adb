def send_command(device, command):
    response = device.shell(command)
    return response


def pull_command(device, device_path, local_path):
    device.pull(device_path, local_path)
    return None

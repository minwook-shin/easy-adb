import os
import subprocess

from adb_shell.adb_device import AdbDeviceTcp


def run_adb_server():
    os.environ["ADB_VENDOR_KEYS"] = "adb_key"
    home_directory = os.path.expanduser("~")

    try:
        subprocess.run(["chmod", "+x", os.path.join(home_directory, "adb/platform-tools/adb")], check=True)
        subprocess.run([os.path.join(home_directory, "adb/platform-tools/adb"), "kill-server"], check=True)
        subprocess.run([os.path.join(home_directory, "adb/platform-tools/adb"), "start-server"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error starting ADB server: {e}")


def connect_device(signer, wifi_ip='', wifi_port=5555):
    device = AdbDeviceTcp(wifi_ip, wifi_port)
    device.connect(rsa_keys=[signer], auth_timeout_s=60)
    return device

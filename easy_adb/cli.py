import argparse

from easy_adb.modules.command import send_command
from easy_adb.modules.download import download_adb_binary
from easy_adb.modules.server import run_adb_server, connect_device
from easy_adb.modules.signing import set_signer


def main():
    parser = argparse.ArgumentParser(description='ADB CLI Tool')
    parser.add_argument('--ip', required=True, help='WIFI IP address')
    parser.add_argument('--port', required=True, default=5555, type=int, help='WIFI port number')
    parser.add_argument('--adb-command', required=True, help='ADB command to execute')

    args = parser.parse_args()

    download_adb_binary()
    run_adb_server()
    sign = set_signer()
    test_device = connect_device(sign, args.ip, args.port)
    result = send_command(test_device, args.adb_command)
    print(result)


if __name__ == '__main__':
    main()

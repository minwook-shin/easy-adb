# easy-adb

## Introduction

easy-adb is a tool written in Python that simplifies the use of Android Debug Bridge (ADB) commands. 

With this tool, you can easily perform tasks such as starting an ADB server, connecting to an Android device, and executing ADB commands using Python code.

Important : This project does not contain any content from the Android SDK Platform-Tools. 
Necessary libraries must be downloaded separately by the download_adb_binary command.

## Installation

If Python >= 3.9 is installed, you can install easy-adb with the following command:

```shell
pip install easy-adb
```

## Usage

easy-adb can be used through a command-line interface (CLI). 

Here is the basic way to use easy-adb:

```shell
python -m easy_adb.cli --ip [device IP] --port [port number] --adb-command [ADB command to execute]
```

replace [device IP], [port number], and [ADB command to execute] with the actual values.

or you can use easy-adb in Python code:

```python
from easy_adb import run_adb_server, set_signer, connect_device, send_command, download_adb_binary

# equivalent to: easy-adb --ip 192.168.0.1 --port=5555 --adb-command="getprop ro.product.model"

# download_adb_binary()  # optional
run_adb_server()
test_device = connect_device(set_signer(), "192.168.0.1", 5555)
result = send_command(test_device, "getprop ro.product.model")
```

## Features

easy-adb provides the following features:

* ADB Server Management: Start the ADB server from Python code.
* Device Connection Management: Connect to Android devices using WI-FI IP address and port number.
* ADB Command Execution: Execute ADB command and retrieve output.

## License

This project is distributed under the LGPLv3 license. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Please note that the easy-adb library does not take any responsibility for the download and use of the Android SDK Platform-Tools. 

Users are responsible for ensuring that they download and use these tools in a manner that is in compliance with the terms and conditions set forth by the original provider. 

## Contact

For bug reports about this project, please submit them through the GitHub issue tracker.
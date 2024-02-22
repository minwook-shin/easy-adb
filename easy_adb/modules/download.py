import os
import platform
import zipfile

import requests

from easy_adb.resource import agreement_file_path


def __get_user_agreement(agreement):
    print(agreement_file_path)
    with open(agreement_file_path, "r") as agreement_file:
        print(agreement_file.read())

    if agreement is True:
        print("Terms automatically accepted by code.")
        user_input = "y"
    else:
        user_input = input(f"Do you agree to the terms in {agreement_file_path}? (y/n): ").lower()
    return user_input == "y"


def download_adb_binary(agreement: bool = False):
    home_directory = os.path.expanduser("~")
    binary_url = ""
    if platform.system() == "Darwin":
        binary_url = "https://dl.google.com/android/repository/platform-tools-latest-darwin.zip"
    elif platform.system() == "Linux":
        binary_url = "https://dl.google.com/android/repository/platform-tools-latest-linux.zip"
    elif platform.system() == "Windows":
        binary_url = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
    download_path = os.path.join(home_directory, "platform-tools-latest-darwin.zip")
    extract_path = os.path.join(home_directory, "adb")

    if not os.path.isdir(extract_path) and __get_user_agreement(agreement):
        b = requests.get(binary_url).content
        with open(download_path, 'wb') as f:
            f.write(b)

        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        os.remove(download_path)
        print("ADB binary has been downloaded and installed successfully.")
    else:
        print("Installation aborted. You did not agree to the terms or already installed.")


if __name__ == "__main__":
    download_adb_binary()

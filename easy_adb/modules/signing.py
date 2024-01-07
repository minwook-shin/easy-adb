import os

from adb_shell.auth.sign_pythonrsa import PythonRSASigner

os.environ["ADB_VENDOR_KEYS"] = "adb_key"


def set_signer():
    if not os.path.isfile('adb_key'):
        from adb_shell.auth.keygen import keygen
        keygen('adb_key')

    adb_key = 'adb_key'
    with open(adb_key) as f:
        private = f.read()
    with open(adb_key + '.pub') as f:
        public = f.read()
    signer = PythonRSASigner(public, private)
    return signer

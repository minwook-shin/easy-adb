from easy_adb import run_adb_server, set_signer, connect_device, send_command, download_adb_binary

# equivalent to: easy-adb --ip 192.168.0.1 --port=5555 --adb-command="getprop ro.product.model"

download_adb_binary()
run_adb_server()
sign = set_signer()
test_device = connect_device(sign, "192.168.0.1", 5555)
result = send_command(test_device, "getprop ro.product.model")
print(result)

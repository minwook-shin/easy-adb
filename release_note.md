# Release Notes

## [0.1.1](https://pypi.org/project/easy-adb/0.1.0/) (2024-03-05)

* Added missing USB dependency package

## [0.1.0](https://pypi.org/project/easy-adb/0.1.0/) (2024-03-05)

### New Features

* Added USB connection support


## [0.0.3](https://pypi.org/project/easy-adb/0.0.3/) (2024-02-22)

### New Features

* Added option to accept terms boolean when console input is not possible

## [0.0.2](https://pypi.org/project/easy-adb/0.0.2/) (2024-02-21)

### New Features

* pull command

```python
result = send_command(test_device, "screencap /sdcard/screen-tmp.png ")
pull_command(test_device, "/sdcard/screen-tmp.png", "screen-tmp.png")
```

## [0.0.1](https://pypi.org/project/easy-adb/0.0.1/) (2024-01-07)

### New Features

* initial release
  * ADB Server Running
  * Device Connection
  * ADB Command Execution

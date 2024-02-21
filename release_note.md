# Release Notes

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

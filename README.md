# Homecontrol-Logg-Analyzer
A logg analyzer for the homecontrol project (work in progress)

### Purpose
A logg analyzer which shall in the end visualize the logged events of my Homecontrol system

E.g.:
- Temperature
- Humidity
- Presence (bluetooth device in range or not) (BTDevice)

### Example Logfile
```
TCPManager.cpp Line: 223 2019-02-16 17:06:26:582 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:06:26:734 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:06:26:734 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:06:26:886 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:06:26:886 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:06:43:124 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:06:43:124 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:06:43:277 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:06:43:277 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:06:43:431 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:06:43:431 Trying to send a MANDOLYN_SENSOR MESSAGE
BluetoothDevice.cpp Line: 85 2019-02-16 17:06:45:554 BTDevice TempIphone Yes in Range
BluetoothDevice.cpp Line: 85 2019-02-16 17:06:46:933 BTDevice Apple Watch von Andreas Yes in Range
BluetoothDevice.cpp Line: 85 2019-02-16 17:06:48:617 BTDevice Ankes iPhone Yes in Range
BluetoothManager.cpp Line: 103 2019-02-16 17:06:48:617 -------------------------------------------
BluetoothDevice.cpp Line: 85 2019-02-16 17:07:16:003 BTDevice TempIphone Yes in Range
TCPManager.cpp Line: 52 2019-02-16 17:07:16:757 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:16:757 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:07:16:901 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:16:901 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:07:17:053 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:17:053 Trying to send a MANDOLYN_SENSOR MESSAGE
BluetoothDevice.cpp Line: 78 2019-02-16 17:07:23:999 BTDevice Apple Watch von Andreas No Not in Range
BluetoothDevice.cpp Line: 85 2019-02-16 17:07:26:020 BTDevice Ankes iPhone Yes in Range
BluetoothManager.cpp Line: 103 2019-02-16 17:07:26:020 -------------------------------------------
TCPManager.cpp Line: 52 2019-02-16 17:07:26:596 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:26:596 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:07:26:750 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:26:750 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:07:26:851 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:26:851 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:07:43:142 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:43:142 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:07:43:286 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:43:286 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:07:43:399 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:43:399 Trying to send a MANDOLYN_SENSOR MESSAGE
BluetoothDevice.cpp Line: 85 2019-02-16 17:07:45:378 BTDevice TempIphone No Not in Range
BluetoothDevice.cpp Line: 85 2019-02-16 17:07:45:815 BTDevice Apple Watch von Andreas No Not in Range
BluetoothDevice.cpp Line: 78 2019-02-16 17:07:53:815 BTDevice Ankes iPhone No Not in Range
BluetoothManager.cpp Line: 103 2019-02-16 17:07:53:815 -------------------------------------------
TCPManager.cpp Line: 52 2019-02-16 17:08:16:718 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:08:16:718 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:08:16:872 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:08:16:872 Trying to send a MANDOLYN_SENSOR MESSAGE
TCPManager.cpp Line: 52 2019-02-16 17:08:17:025 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:08:17:025 Trying to send a MANDOLYN_SENSOR MESSAGE
```

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
BluetoothDevice.cpp Line: 85 2019-02-16 17:06:45:554 BTDevice TempIphone Yes in Range
BluetoothDevice.cpp Line: 85 2019-02-16 17:06:46:933 BTDevice Apple Watch von Andreas Yes in Range
BluetoothDevice.cpp Line: 85 2019-02-16 17:06:48:617 BTDevice Ankes iPhone Yes in Range
BluetoothManager.cpp Line: 103 2019-02-16 17:06:48:617 -------------------------------------------
BluetoothDevice.cpp Line: 85 2019-02-16 17:07:16:003 BTDevice TempIphone Yes in Range
TCPManager.cpp Line: 52 2019-02-16 17:07:16:757 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:16:757 Trying to send a MANDOLYN_SENSOR MESSAGE ID: 10 Temp: 15.4 Humidity: 23
TCPManager.cpp Line: 52 2019-02-16 17:07:16:901 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:16:901 Trying to send a MANDOLYN_SENSOR MESSAGE ID: 10 Temp: 15.4 Humidity: 23
TCPManager.cpp Line: 52 2019-02-16 17:07:17:053 Handled id:17
TCPManager.cpp Line: 223 2019-02-16 17:07:17:053 Trying to send a MANDOLYN_SENSOR MESSAGE ID: 10 Temp: 15.5 Humidity: 23
BluetoothDevice.cpp Line: 78 2019-02-16 17:07:23:999 BTDevice Apple Watch von Andreas No Not in Range
BluetoothDevice.cpp Line: 85 2019-02-16 17:07:26:020 BTDevice Ankes iPhone Yes in Range
BluetoothManager.cpp Line: 103 2019-02-16 17:07:26:020 -------------------------------------------
BluetoothDevice.cpp Line: 85 2019-02-16 17:07:45:378 BTDevice TempIphone No Not in Range
BluetoothDevice.cpp Line: 85 2019-02-16 17:07:45:815 BTDevice Apple Watch von Andreas No Not in Range
BluetoothDevice.cpp Line: 78 2019-02-16 17:07:53:815 BTDevice Ankes iPhone No Not in Range
BluetoothManager.cpp Line: 103 2019-02-16 17:07:53:815 -------------------------------------------
TCPManager.cpp Line: 52 2019-05-13 16:33:44:643 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:33:44:643 Sending a MANDOLYN_SENSOR MESSAGE ID: 12 Temp: 22.2 Humidity: 14
TCPManager.cpp Line: 52 2019-05-13 16:33:44:804 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:33:44:805 Sending a MANDOLYN_SENSOR MESSAGE ID: 12 Temp: 22.2 Humidity: 14
TCPManager.cpp Line: 52 2019-05-13 16:33:50:884 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:33:50:884 Sending a MANDOLYN_SENSOR MESSAGE ID: 11 Temp: 22.9 Humidity: 14
TCPManager.cpp Line: 52 2019-05-13 16:33:51:036 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:33:51:037 Sending a MANDOLYN_SENSOR MESSAGE ID: 11 Temp: 23 Humidity: 14
TCPManager.cpp Line: 52 2019-05-13 16:33:51:127 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:33:51:128 Sending a MANDOLYN_SENSOR MESSAGE ID: 11 Temp: 23 Humidity: 14
BluetoothManager.cpp Line: 103 2019-05-13 16:33:57:968 -------------------------------------------
TCPManager.cpp Line: 52 2019-05-13 16:34:23:547 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:34:23:547 Sending a MANDOLYN_SENSOR MESSAGE ID: 21 Temp: 10.4 Humidity: 64
TCPManager.cpp Line: 52 2019-05-13 16:34:23:638 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:34:23:639 Sending a MANDOLYN_SENSOR MESSAGE ID: 21 Temp: 10.5 Humidity: 64
TCPManager.cpp Line: 52 2019-05-13 16:34:23:800 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:34:23:801 Sending a MANDOLYN_SENSOR MESSAGE ID: 21 Temp: 10.5 Humidity: 64
BluetoothManager.cpp Line: 103 2019-05-13 16:34:27:753 -------------------------------------------
TCPManager.cpp Line: 52 2019-05-13 16:34:44:640 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:34:44:641 Sending a MANDOLYN_SENSOR MESSAGE ID: 12 Temp: 22.2 Humidity: 14
TCPManager.cpp Line: 52 2019-05-13 16:34:44:781 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:34:44:782 Sending a MANDOLYN_SENSOR MESSAGE ID: 12 Temp: 22.2 Humidity: 14
TCPManager.cpp Line: 52 2019-05-13 16:34:44:934 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:34:44:934 Sending a MANDOLYN_SENSOR MESSAGE ID: 12 Temp: 22.2 Humidity: 14
TCPManager.cpp Line: 52 2019-05-13 16:34:47:597 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:34:47:598 Sending a MANDOLYN_SENSOR MESSAGE ID: 11 Temp: 14.2 Humidity: 21
TCPManager.cpp Line: 52 2019-05-13 16:34:50:850 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:34:50:851 Sending a MANDOLYN_SENSOR MESSAGE ID: 11 Temp: 22.9 Humidity: 14
TCPManager.cpp Line: 52 2019-05-13 16:34:50:991 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:34:50:992 Sending a MANDOLYN_SENSOR MESSAGE ID: 11 Temp: 23 Humidity: 14
TCPManager.cpp Line: 52 2019-05-13 16:34:51:092 Handled id:17
TCPManager.cpp Line: 225 2019-05-13 16:34:51:093 Sending a MANDOLYN_SENSOR MESSAGE ID: 11 Temp: 23 Humidity: 14
BluetoothManager.cpp Line: 103 2019-05-13 16:34:57:547 -------------------------------------------


```

Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

======== RESTART: C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py ========
❌ Could not find DLL folder at C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\libusb_package\_platform\_windows\x64
Attempting to connect to usb://0...
Couldn't load link driver: No backend available

Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crazyflie\__init__.py", line 250, in open_link
    self.link = cflib.crtp.get_link_driver(
                ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        link_uri, self.link_statistics.radio_link_statistics_callback, self._link_error_cb)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\__init__.py", line 99, in get_link_driver
    instance.connect(uri, radio_link_statistics_callback, link_error_callback)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\usbdriver.py", line 84, in connect
    self.cfusb = CfUsb(devid=int(uri_data.group(1)))
                 ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 87, in __init__
    devices = _find_devices()
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 66, in _find_devices
    devices = usb.core.find(idVendor=USB_VID, idProduct=USB_PID, find_all=1,
                            backend=backend)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 1321, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available

❌ Still No Connection. Please check Zadig one last time.

======== RESTART: C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py ========
Searching for libusb-1.0.dll...
✅ FOUND DLL AT: C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\libusb_package
Attempting to connect to usb://0...
Couldn't load link driver: No backend available

Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crazyflie\__init__.py", line 250, in open_link
    self.link = cflib.crtp.get_link_driver(
                ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        link_uri, self.link_statistics.radio_link_statistics_callback, self._link_error_cb)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\__init__.py", line 99, in get_link_driver
    instance.connect(uri, radio_link_statistics_callback, link_error_callback)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\usbdriver.py", line 84, in connect
    self.cfusb = CfUsb(devid=int(uri_data.group(1)))
                 ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 87, in __init__
    devices = _find_devices()
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 66, in _find_devices
    devices = usb.core.find(idVendor=USB_VID, idProduct=USB_PID, find_all=1,
                            backend=backend)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 1321, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available

❌ Connection failed. Check Zadig 'Interface 1'.

======== RESTART: C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py ========
Configuring USB Backend...
❌ Could not find libusb-1.0.dll!

======== RESTART: C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py ========
❌ The path you pasted does not exist: PASTE_YOUR_PATH_HERE
⚠️ Using fallback path: C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\libusb_package
Attempting to connect to usb://0 ...
Couldn't load link driver: No backend available

Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crazyflie\__init__.py", line 250, in open_link
    self.link = cflib.crtp.get_link_driver(
                ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        link_uri, self.link_statistics.radio_link_statistics_callback, self._link_error_cb)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\__init__.py", line 99, in get_link_driver
    instance.connect(uri, radio_link_statistics_callback, link_error_callback)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\usbdriver.py", line 84, in connect
    self.cfusb = CfUsb(devid=int(uri_data.group(1)))
                 ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 87, in __init__
    devices = _find_devices()
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 66, in _find_devices
    devices = usb.core.find(idVendor=USB_VID, idProduct=USB_PID, find_all=1,
                            backend=backend)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 1321, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available

❌ FAILED: The computer sees the DLL, but cannot talk to the drone.
   1. Check Zadig: Ensure 'Interface 1' is 'libusb-win32'.
   2. Try a different USB cable.

======== RESTART: C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py ========
❌ The path you pasted does not exist: PASTE_YOUR_PATH_HERE
⚠️ Using fallback path: C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\libusb_package
Attempting to connect to usb://0 ...
Couldn't load link driver: No backend available

Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crazyflie\__init__.py", line 250, in open_link
    self.link = cflib.crtp.get_link_driver(
                ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        link_uri, self.link_statistics.radio_link_statistics_callback, self._link_error_cb)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\__init__.py", line 99, in get_link_driver
    instance.connect(uri, radio_link_statistics_callback, link_error_callback)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\usbdriver.py", line 84, in connect
    self.cfusb = CfUsb(devid=int(uri_data.group(1)))
                 ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 87, in __init__
    devices = _find_devices()
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 66, in _find_devices
    devices = usb.core.find(idVendor=USB_VID, idProduct=USB_PID, find_all=1,
                            backend=backend)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 1321, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available

❌ FAILED: The computer sees the DLL, but cannot talk to the drone.
   1. Check Zadig: Ensure 'Interface 1' is 'libusb-win32'.
   2. Try a different USB cable.

======== RESTART: C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py ========
--- DRONE HARDWARE PROBE ---
Traceback (most recent call last):
  File "C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py", line 11, in <module>
    dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 1321, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available

======== RESTART: C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py ========
✅ DLL directory added: C:\Users\user\AppData\Local\Programs\Python\Python313\DLLs
Opening link to usb://0 ...
Couldn't load link driver: No backend available

Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crazyflie\__init__.py", line 250, in open_link
    self.link = cflib.crtp.get_link_driver(
                ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        link_uri, self.link_statistics.radio_link_statistics_callback, self._link_error_cb)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\__init__.py", line 99, in get_link_driver
    instance.connect(uri, radio_link_statistics_callback, link_error_callback)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\usbdriver.py", line 84, in connect
    self.cfusb = CfUsb(devid=int(uri_data.group(1)))
                 ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 87, in __init__
    devices = _find_devices()
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 66, in _find_devices
    devices = usb.core.find(idVendor=USB_VID, idProduct=USB_PID, find_all=1,
                            backend=backend)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 1321, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available

❌ Connection failed: Couldn't load link driver: No backend available

Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crazyflie\__init__.py", line 250, in open_link
    self.link = cflib.crtp.get_link_driver(
                ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        link_uri, self.link_statistics.radio_link_statistics_callback, self._link_error_cb)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\__init__.py", line 99, in get_link_driver
    instance.connect(uri, radio_link_statistics_callback, link_error_callback)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\usbdriver.py", line 84, in connect
    self.cfusb = CfUsb(devid=int(uri_data.group(1)))
                 ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 87, in __init__
    devices = _find_devices()
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 66, in _find_devices
    devices = usb.core.find(idVendor=USB_VID, idProduct=USB_PID, find_all=1,
                            backend=backend)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 1321, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available

❌ FAILED: Still no connection.
1. Check Zadig: Interface 1 must be 'libusb-win32'.
2. Try unplugging and replugging the drone.

======== RESTART: C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py ========
✅ DLL directory added: C:\Users\user\AppData\Local\Programs\Python\Python313\DLLs
Opening link to usb://0 ...
Couldn't load link driver: No backend available

Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crazyflie\__init__.py", line 250, in open_link
    self.link = cflib.crtp.get_link_driver(
                ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        link_uri, self.link_statistics.radio_link_statistics_callback, self._link_error_cb)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\__init__.py", line 99, in get_link_driver
    instance.connect(uri, radio_link_statistics_callback, link_error_callback)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\usbdriver.py", line 84, in connect
    self.cfusb = CfUsb(devid=int(uri_data.group(1)))
                 ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 87, in __init__
    devices = _find_devices()
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 66, in _find_devices
    devices = usb.core.find(idVendor=USB_VID, idProduct=USB_PID, find_all=1,
                            backend=backend)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 1321, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available

❌ Connection failed: Couldn't load link driver: No backend available

Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crazyflie\__init__.py", line 250, in open_link
    self.link = cflib.crtp.get_link_driver(
                ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        link_uri, self.link_statistics.radio_link_statistics_callback, self._link_error_cb)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\__init__.py", line 99, in get_link_driver
    instance.connect(uri, radio_link_statistics_callback, link_error_callback)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\usbdriver.py", line 84, in connect
    self.cfusb = CfUsb(devid=int(uri_data.group(1)))
                 ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 87, in __init__
    devices = _find_devices()
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 66, in _find_devices
    devices = usb.core.find(idVendor=USB_VID, idProduct=USB_PID, find_all=1,
                            backend=backend)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 1321, in find
    raise NoBackendError('No backend available')
usb.core.NoBackendError: No backend available

❌ FAILED: Still no connection.
1. Check Zadig: Interface 1 must be 'libusb-win32'.
2. Try unplugging and replugging the drone.

======== RESTART: C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py ========
✅ Found Driver at: C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\libusb_package\libusb-1.0.dll
Attempting to connect to usb://0 ...
Couldn't load link driver: Operation not supported or unimplemented on this platform

Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crazyflie\__init__.py", line 250, in open_link
    self.link = cflib.crtp.get_link_driver(
                ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        link_uri, self.link_statistics.radio_link_statistics_callback, self._link_error_cb)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\__init__.py", line 99, in get_link_driver
    instance.connect(uri, radio_link_statistics_callback, link_error_callback)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\crtp\usbdriver.py", line 84, in connect
    self.cfusb = CfUsb(devid=int(uri_data.group(1)))
                 ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 87, in __init__
    devices = _find_devices()
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\cflib\drivers\cfusb.py", line 70, in _find_devices
    if d.manufacturer == 'Bitcraze AB':
       ^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 912, in manufacturer
    self._manufacturer = util.get_string(self, self.iManufacturer)
                         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\util.py", line 307, in get_string
    langids = dev.langids
              ^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 865, in langids
    self._langids = util.get_langids(self)
                    ~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\util.py", line 262, in get_langids
    buf = get_descriptor(
                dev,
    ...<2 lines>...
                0
            )
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\control.py", line 172, in get_descriptor
    desc = dev.ctrl_transfer(
            bmRequestType = bmRequestType,
    ...<2 lines>...
            wIndex = wIndex,
            data_or_wLength = desc_size)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 1082, in ctrl_transfer
    self._ctx.managed_open()
    ~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 113, in wrapper
    return f(self, *args, **kwargs)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\core.py", line 132, in managed_open
    self.handle = self.backend.open_device(self.dev)
                  ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\backend\libusb1.py", line 808, in open_device
    return _DeviceHandle(dev)
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\backend\libusb1.py", line 656, in __init__
    _check(_lib.libusb_open(self.devid, byref(self.handle)))
    ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\usb\backend\libusb1.py", line 600, in _check
    raise NotImplementedError(_strerror(ret))
NotImplementedError: Operation not supported or unimplemented on this platform

❌ Backend is now working, but the Drone is not responding.
   ACTION: Open Zadig and set Interface 1 to 'libusb-win32'.

======== RESTART: C:/Users/user/Desktop/drone_gcs/TEST_CRAZYFILE_RAW.py ========
✅ Found Driver at: C:\Users\user\AppData\Local\Programs\Python\Python313\Lib\site-packages\libusb_package\libusb-1.0.dll
Attempting to connect to usb://0 ...
🎉🎉 SUCCESS: CONNECTED! 🎉🎉
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00
Batt: 4.19V | X: 0.00

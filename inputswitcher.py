import pyudev
import evdev
import subprocess

def find_device(device_name):
    """Search for an input device with the given name."""
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

    for device in devices:
        if device.name == device_name:
            print(f"Found device: {device.name} at {device.path}")
            return device.path  # Return the first match

    print(f"No device named '{device_name}' found.")
    return None


# Search for the Logitech MX Ergo
device_path = find_device("Logitech MX Ergo")

# Create a udev context
context = pyudev.Context()

# Monitor USB input devices
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='input')  # Only listen to input devices (e.g., keyboard, mouse)

while True:
    print("Waiting for keyboard removal...")

    # Iterate through events
    for device in iter(monitor.poll, None):
        device_name = device.get('NAME', '')
    #    print(f"Event: {device.action.upper()} | Device: {device_name}")
    #    for key, value in device.properties.items():
    #        print(f"  {key}: {value}")
    #    print("-" * 50)
        if device.action == 'remove' and "MX MCHNCL" in device_name:
            print(f"Keyboard '{device_name}' removed! ({device.device_path})")
            break  # Exit after detecting the removal

    # Open the input device
    mouse_device = evdev.InputDevice(device_path)

    # Print the device name for reference
    print(f"Listening for events on {mouse_device.name} ...")

    # Block until an event occurs
    for event in mouse_device.read_loop():
        # Check if the event type is a valid input event (e.g., mouse or keyboard movement)
        if event.type != evdev.ecodes.EV_SYN:  # Ignore sync events
            print(f"Event detected: {event}")
            break  # Exit after first event

    # Once an event is detected, fetch keyboard
    try:
        print("Running ssh to execute switch_to_host3.bat on vm-win11")
        subprocess.run(['ssh', 'rainer1956@vm-win11', 'switch_to_host3.bat'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running ssh: {e}")







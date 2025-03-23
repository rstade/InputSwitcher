# This is a sample Python script.
import subprocess
from pynput import mouse

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import hid


def on_event(x, y, button=None, pressed=None, dx=None, dy=None):
    """Callback function to handle any mouse movement, click, or scroll."""
    print("Mouse event detected!")
    listener.stop()  # Stop listener after the first event


#
#
# def find_evoluent_mouse():
#     """Search for an Evoluent Mouse among connected HID devices."""
#     devices = hid.enumerate()
#     found = False
#
#     for device in devices:
#         product_name = device.get("product_string", "").lower()
#         #print(f"Found device: {product_name}")
#
#         if "evoluent" in product_name:
#             found = True
#             return device
#
#     if not found:
#         return None
#
#
# def wait_for_mouse_event(evoluent):
#     """Blocks until the Evoluent Mouse sends an event (move/click)."""
#     try:
#         print(f"🔄 Waiting for input from Evoluent Mouse ")
#         vendor_id = evoluent.get("vendor_id", "")
#         product_id = evoluent.get("product_id", "")
#         device = hid.Device(vendor_id, product_id)
#         while True:
#             data = device.read(64)  # Read up to 64 bytes (adjust if needed)
#             if data:
#                 print(f"🎯 Event Received: {data}")
#                 break  # Exit after receiving the first event
#
#     except OSError as e:
#         print(f"❌ Error: {e}")
#         print("Make sure the mouse is connected and not in use by another program.")


if __name__ == "__main__":

    # Create a listener instance
    listener = mouse.Listener(on_move=on_event, on_click=on_event, on_scroll=on_event)

    # Start listening (blocking until an event happens)
    listener.start()
    listener.join()  # Blocks execution until an event occurs
    try:
        print("Starting ssh to execute  switch_to_channel2.sh  on fedora-pc")
        subprocess.run(['ssh', 'rainer1956@fedora-pc.fritz.box', "switch_to_channel2.sh"])
    except subprocess.CalledProcessError as e:
        print(f"Error running ssh: {e}")


import can
print("Connecting to Vector CAN interface...")

# Configuration for vector Channels (0 es CAN1, 1 es CAN2)
bus = can.Bus(
    interface='vector',
    channel=[1],
    bitrate=500000,
    app_name='PythonApp' # Nombre de la aplicación que diste en Vector Hardware Config
)

# Send a message on CAN bus
msg = can.Message(arbitration_id=0x123, data=[0x11, 0x22, 0x33], is_extended_id=False)
try:
    bus.send(msg)
    print(f"Message sent successfully: {msg}")
except can.CanError:
    print("Error sending message")

# Reading messages from CAN bus
print("Listening to the CAN bus...")
for message in bus:
    print(message)
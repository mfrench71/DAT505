from mosquitto import *
from serial import *
from random import *

# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino
board = Serial("COM3",9600,timeout=2)

randomID = random()
client = Mosquitto("LightSubscriber" + str(randomID))
client.connect("10.212.61.136")

client.subscribe("/lights")

# Write a function to handle the incoming message
def messageReceived(broker, obj, msg):
    global client   
    payload = msg.payload.decode()
    print("Message " + msg.topic + " containing: " + payload)
    #client = None
    
    # Clear any previous old data waiting in the buffer
    # board.readall()

    # Write out a string to the serial port
    message = "Hello there Arduino\n"
    board.write(payload.encode())
    #print("You just said: Hello there Arduino")

    # Read back in and print the response from the serial port, then close it
    input = board.readline()
    #print("Arduino replied: " + input)
    #board.close()

# Register the incoming message handler
client.on_message = messageReceived

# While the client still exists, ask it to process incoming messages
while (client != None): client.loop()


    

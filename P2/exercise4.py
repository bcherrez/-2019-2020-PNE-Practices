from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.45"
PORT = 8080

c = Client(IP, PORT)

print(c)

# -- Send a message to the server
c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")
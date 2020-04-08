
import socket


PORT = 8081
IP = "192.168.1.105"

number_con = 0

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.bind((IP, PORT))
    socket.listen(50)

    while True:
        print("Waiting for connections at", IP, ",", PORT)
        (clientsocket, address) = socket.accept()

        print("CONNECTION:", number_con, " From the IP: ", client_ip_port)

        msg = clientsocket.recv(2000)
        print("Message from client: ", end="")

        message = "Hello there from the server"
        send_bytes = str.encode(message)

        clientsocket.send(send_bytes)
        print(message)

        clientsocket.close()

except socket.error:
    print("Problems using port ".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    socket.close()
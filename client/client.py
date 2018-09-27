import socket

RS_PORT = 60020

def rs_connect():
    sa_sameas_myaddr = socket.gethostbyname(socket.gethostname())

    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Created client socket")
    except socket.error as err:
        print("Unable to create socket", err)

    connection.connect((sa_sameas_myaddr, RS_PORT))

    return connection

def main():
    connection = rs_connect()

    connection.send("google.com".encode("utf-8"))

    result = connection.recv(100).decode('utf-8')

    print("Received response: ", result)

main()
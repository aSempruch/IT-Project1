import socket as TS_ServerSocket
from helpers.customPrint import ts_print
from helpers.loadFromFile import loadFromFile
import sys

PORT = 60030
dns_records ={}

def runServer():
    try:
        serverConnection = TS_ServerSocket.socket(TS_ServerSocket.AF_INET, TS_ServerSocket.SOCK_STREAM)
	print("Server Socket created")
    except TS_ServerSocket.error as err:
	ts_print("Error connecting to TS_Server")
	sys.exit()

    #bind socket to addr
    server_binding = ('', PORT)
    serverConnection.bind(server_binding)

    #listen for connection
    serverConnection.listen(1)

    hostname = TS_ServerSocket.gethostname()
    ts_print("Hostname: ", hostname)

    host_ip = (TS_ServerSocket.gethostbyname(hostname))
    ts_print("IP Address: ", host_ip)

    #wait for connection
    connected_socket, addr = TS_ServerSocket.accept()

    query = TS_ServerSocket.recv(100).decode('utf-8')
    ts_print("query may have been received")
    connected_socket.send(hostnameLookup(query)).encode('utf-8')

    serverConnection.close()
    exit()

def hostnameLookup(query):
    hostname = query.strip()
    if hostname in dns_records:
	entry = dns_records[hostname]
	return hostname + " " + entry["ip"] + " " + entry["flag"]

    return hostname + "-  " + "Error: HOST NOT FOUND"  

def loadFile():
    file = open("...PROJ-DNSTS.txt", r)

	global dns_records
    dns_records = loadFromFile(file)
	ts_print("Finished loading file")
    


def main():

    loadFile()
    while True:
         runServer()

    #runServer.close()
    sys.exit()

main()	

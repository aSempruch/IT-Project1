import socket
from helpers.customPrint import rs_print as xprint
from helpers.loadFromFile import loadFromFile

PORT = 60020
dnsRecords = {}

def lookupHostname(query):

    hostname = query.strip()

    # Hostname is in DNS records
    if hostname in dnsRecords:
        entry = dnsRecords[hostname]
        return hostname + " " + entry["ip"] + " " + entry["flag"]

    # Hostname not found in DNS records
    return dnsRecords['NS'] + ' - NS'

def startServer():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        xprint("Socket Created")
    except socket.error as err:
        xprint("Error Opening Socket", err)
        exit(10)

    connection.bind(('', PORT))
    connection.listen(1)

    host = socket.gethostname()
    xprint("Hostname:", host)

    localhost_ip = (socket.gethostbyname(host))
    xprint("IP:", localhost_ip)

    return connection

def runService(connection):
    csockid, addr = connection.accept()
    xprint("Got connection request from", str(addr))

    query = csockid.recv(100).decode('utf-8')
    xprint("Lookup from client:", query)

    csockid.send(lookupHostname(query).encode('utf-8'))

def loadFile():
    # Read file into data structure
    with open("../PROJI-DNSRS.txt", "r") as dnsFile:
        global dnsRecords
        dnsRecords = loadFromFile(dnsFile)
        xprint("Loaded DNSRS file")

def main():

    loadFile()

    connection = startServer()

    # Accept multiple connections
    while True:
        runService(connection)

    connection.close()

main()
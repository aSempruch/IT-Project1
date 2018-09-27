import socket

port = 60020

def xprint(string, value = ""):
    print "[RS] " + string + " " + value

def lookupHostname(query):
    xprint("Looking up ", query)

def startServer():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        xprint("Socket Created")
    except socket.error as err:
        xprint("Error Opening Socket", err)
        exit()

    ss.bind(('', port))
    ss.listen(1)

    host = socket.gethostname()
    xprint("Hostname:", host)

    localhost_ip = (socket.gethostbyname(host))
    xprint("IP:", localhost_ip)

    return ss

def runService(ss):
    csockid, addr = ss.accept()
    xprint("Got connection request from", addr)

    query = csockid.recv(100).decode('utf-8')
    xprint("Lookup from client:", query)

    csockid.send(lookupHostname(query))

def main():
    ss = startServer()

    # Accept multiple connections
    while True:
        runService(ss)

    ss.close()

main()
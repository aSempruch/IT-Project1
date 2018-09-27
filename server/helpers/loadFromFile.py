def loadFromFile(dnsFile):
    records = {}

    for line in dnsFile:
        split = line.strip().split(" ")
        records[split[0]] = {
            "ip": split[1],
            "flag": split[2]
        }
    return records
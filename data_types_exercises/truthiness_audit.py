# Truthiness Audit
# Write a class OpenPort with attributes port and status, and define __bool__ so that the instance is truthy only when status == "open".

class OpenPort:
    def __init__(self, port, status):
        self.port = port
        self.status = status

    def __bool__(self):
        return self.status == "open"
    
port80 = OpenPort(80, "closed")
port443 = OpenPort(443, "open")

if port80:
    print("80 Open")
if port443:
    print("443 Open")

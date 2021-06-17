# Python UDP Server/Client Implementation

This is an implementation of UDP Server/Client based on excellent documentation from [sockerserver] (https://docs.python.org/3/library/socketserver.html) 
<br/>
<br/>

---
## How to use
### UDP Server
Usage of udpServer.py:
```
python udpServer.py [--host HOST default=localhost] [--port PORT default=10000]

Example:
python udpServer.py --host=localhost --port=20000
```

The above code will start a UDP server. The server will print any message received from client. 
To stop the server press 'Ctr+C'.

Note:  
When localhost is used, the underlying code will find the current hostname.  
Using localhost will work if the client is within the same PC/machine.
<br/>
<br/>

### UDP Client
Usage of udpClient.py:
```
python udpClient.py [--host HOST default=localhost] [--port PORT default=10000]

Example:
python udpClient.py --host=localhost --port=20000
```

The above code will start a UDP client, connecting to the specified host & port. 
We can send any message by typing from the command line. 
To stop the client, type 'exit'. 
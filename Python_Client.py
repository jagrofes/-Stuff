from socket import *
import sys
serverName = sys.argv[1]
serverPortInput = sys.argv[2]
filename = sys.argv[3]	
serverPort = int(serverPortInput,10)
print("Attempting to retrieve file : %s From Host :%s At Port :%s"%(filename, serverName, serverPort, ))

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    header1 = ("GET %s HTTP 1.1 \r\n Accept: text/html \r\n Host: %s"%(filename, serverName))	
	
    clientSocket.send(("%s\r\n\r\n"%(header1)).encode())	

except IOError:

    clientsocket.close()
responseMessage = clientSocket.recv(1024)
clientSocket.close()
print(responseMessage)
sys.exit()	

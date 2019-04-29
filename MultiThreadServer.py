#import socket module
from socket import *
import sys # In order to terminate the program
from _thread import*


serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
#Fill in start
serverPort = 40000
IP = Input('Host : ') #Determine the servername
serverSocket.bind((IP,serverPort))
serverSocket.listen(5)

def clientthread(connectionSocket):
        while True:
            #Establish the connection
            print('Ready to serve...')
            connectionSocket, addr = serverSocket.accept()        
            try:
                message = connectionSocket.recv(1024)
                filename = message.split()[1]                 
                f = open(filename[1:])                      
                outputdata = f.read()	
		        #Send one HTTP header line into socket
                connectionSocket.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'.encode())            
                #Send the content of the requested file to the client
                for i in range(0, len(outputdata)):           
                    connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
        
             
            except IOError:
                #Send response message for file not found
                #Fill in start     
                connectionSocket.send('404 Not Found\r\n\r\n'.encode())			
                #Fill in end
                #Close client socket
                #Fill in start
               
                #Fill in end            
        serverSocket.close
while True:
    connectionSocket, addr = serverSocket.accept()
    print('Connection Established with ' + addr[0] + ":" + str(addr[1])
    _thread.start_new_thread(clientthread, args )

serverSocket.close()

sys.exit()#Terminate the program after sending the corresponding data                                    

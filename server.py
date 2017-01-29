#Name: Shet Neha Nilcant and UTA ID: 1001387308

import socket 
import sys

from threading import Thread

class ServerThread(Thread):
    
     def __init__(self,ip,port,socket):

            #initialise the variables to be used by the thread
            Thread.__init__(self)
            self.ip = ip
            self.port = port
            self.socket = socket
            print "A New thread has been created for Client Socket with IP:"+ip+" Port Number:"+str(port)
    
     def run(self):
    
        try:
            message = self.socket.recv(1024)
            print "Data received from client \n"
            print message+" \n "
            filename = message.split()[1]  #split the data received from the client and read the data at the first index which contains the filename 
            f = open(filename[1:]) #the file name contains '/' ignore it and open the file 
            outputdata = f.read(); #read the open file and save data in the outputdata
            f.close() #close the file
            print "\n Data read from the file \n"
            print outputdata 
            self.socket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n') #send the header to the client with 200 OK status
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                    self.socket.send(outputdata[i])      #send data to the client
        except IOError:
            print 'exception code has been executed'
            self.socket.send('HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n') #send 404 file not found error incase of error
            self.socket.send('<p>HTTP/1.1 404 Not found: The requested file does not exist on this server.</p>');

        #self.socket.send('\n Server Socket family : '+str(serverSocket.family)+'\n Serever socket protocol'+ str(serverSocket.proto)+'\n SocketType'+str(serverSocket.type))
        print "\n data sent to the client";
        self.socket.close()
        print "\n socket is closed";

serverSocket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create the socket object to use IP v4 and TCP.       
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #socket.SO_REUSEADDR, causes the port to be released immediately after the socket is closed.
print serverSocket
#default port
port = 8080

#checks if the port number is specified as the command line argument
if len(sys.argv) > 1:
     port = int(sys.argv[1])

#port would be 8080 if not specified in the command line argument else it would take the value from sys.argv[1]
print "port number from command line "+str(port)   
serverSocket.bind(("127.0.0.1", port)) 
serverSocket.listen(5)
threads = [];
while True:
            
            print "Waiting for incoming connections..."
            conn, address = serverSocket.accept(); #accept the incoming connection through the socket
            
            print "*************** Connection Parameters of Client ****************";
            print 'Got connection from : ', (address[0],address[1])
            print 'Client IP Address : '+address[0];
            print 'Client Port Number : '+str(address[1]);
            print 'Client Host name : localhost'
            print "Peer name : "+str(conn.getpeername())
            print "Socket Family : "+str(conn.family);
            print "Socket Type : "+str(conn.type);
            print "Protocol : "+str(conn.proto)
            newThread = ServerThread(address[0],address[1],conn) #create a new thread for the client connect
            
            newThread.start() #start the thread
            threads.append(newThread) #append the newly created thread to the existing threads array

for thread in threads:
    thread.join()
        

#Name: Shet Neha Nilcant and UTA ID: 1001387308

import socket    #Import socket module
import sys       #Import sys Module           
import time 
from socket import error as socket_error #connection error handling

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # Create a socket object
flag = 0;
if len(sys.argv) > 3:
    ip = sys.argv[1]; #read arg1 from command line which is "localhost"
    port = int(sys.argv[2]); #read arg2 from command line which is "port number"
    try:
        s.connect((ip, port)) #Connect to the given server which is listening to the port number mentioned
        s.send("data /"+str(sys.argv[3])) #send the data (filename) from command line to the server
        start_time = time.time();
        print "Receiving data from server .... "
        while True:
            data = s.recv(1024) # receive the responsefrom the server
            print data
            if not data:        #When no more data is there break 
                break;
        recv_time = time.time();
        roundTripTime = recv_time - start_time; #the round trip time
        s.close #Close the socket when done
        
        print "*************** Connection paramters for Server ****************"
        connectObj = socket.getaddrinfo(ip,port);
        print "Connection object "
        print connectObj;
        print "peer name "+str(s.getpeername  ())
        print "Server IP address : "+ip; #server ip  address
        print "Server port name : "+str(port); #server port name
        print 'Server Host name : localhost'
        print "Peer name : "+str(s.getpeername())
        print "Socket Family : "+str(s.family);
        print "Socket Type : "+str(s.type);
        print "Protocol : "+str(s.proto)
        print "\n ************ RTT ********************";
        print "RTT: "+str(roundTripTime) +" s"; #round trip time for the client request
        
    except socket_error:
        print "Not able to make connection to the server please enter the ip address and port number correctly. \n Terminating Program.... " 
            
else:
    print "please run the program again and pass the appropriate arguments"

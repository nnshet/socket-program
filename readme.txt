#Name: Shet Neha Nilcant and UTA ID: 1001387308

1) The project consist of 2 files.
	 -server.py (multithreaded server)
	 -client.py (Single threaded client)
 
2) Below is the command to start the server through the command line:
 
	python server.py <<port no>>
	
		A user defined port number. 
	
	eg:
	python server.py 9001
	
	If the port number is not specified in the argument it will take 8080 port number from the code

	To test the program through browser hit the below url (server should listen listening on the correct port number):
	
	http://127.0.0.1:9001/check.html
	
	Note : The file could be any file provided it is present on the server.
	
3) Client can request for the file by running the client program through command line or through the browser
	
	Below is the command to start the client program
	
		client.py <<ip_address>> <<port_number>> <<filename>>
	
	eg:client.py 127.0.0.1 9001 check.html
	
	//make sure the port number is same as the server 

	
4) References:
	https://docs.python.org/2/library/socket.html
	https://www.tutorialspoint.com/python/
	http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php

	
	
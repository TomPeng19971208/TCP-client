# TCP-client

This is a tcp client. 
This client will initiate a socket and connect to the designated server. After the connection is established, a HELLO message will be 
sent to the server. Then this client will keep receiving until server sends out end of line signal. If received message is a FIND
command, client will parse this message, perform count operation,  and send back a COUNT message containing how many time the given
char appears in the message. Repeat this process until the received message is a BYE message. When a BYE message is received, 
this client will terminate the connection and print secrete flage contained in the message. 

How this program is tested:
We tested this program by running the script on local machine. If there are bugs, log will appear on system standard output. 
If a secrete flag appears on standard output, we would repeat this process several times to ensure this program is stable. 

challenges:
One challenge for us was to determin when to stop receiving, and how to truncate the message received. 

to run this application:
./client <-p port> <-s> [hostname] [NEU ID]

client will parse parameters and pass them into python program. 

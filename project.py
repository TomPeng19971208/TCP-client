# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import socket
import re
#./client <-p port> <-s> [hostname] [NEU ID]
#the program takes in 4 arguments, [port, ssl, hostname, NEUID]


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
     global isSSL;
     global host;
     global server_port
     global neuid
     
     if (len(sys.argv)!=5):
         print("number of arguments is wrong")
         exit(1)
     else:
         isSSL = sys.argv[2];
         host = sys.argv[3];
         server_port = sys.argv[1]
         neuid = sys.argv[4]
         print("isSSL: " + isSSL)
         print("port: " + server_port)
         print("neuid: " + neuid)
         print("host: " + host)
         #TO DO:
         #1) openconnection
         #2) sendPackage  (see 3700 website)
         #3) countOccurence() and send back the result in format ‘
         #（cs3700spring2019 COUNT [#]\n）using sendPackage()
         #4）receive (cs3700spring2019 BYE [a 64 byte secret flag]\n)
         #from server and extract secret flag
         exit(0)
    
    
def openConnection():
    try:
        sock.connect((host, server_port))
        print("successfully connected")
        
    except Exception as error:
        print("connection failed")
        print(error)
        exit(1)
        
        
def closeConnection():
    sock.close();
    
# send data to server, return server's response
def sendPackage(data):
    message = data.encode()
    sock.sendall(message);
    print("message sent: " + data)
    resp = sock.recv(256)
    return resp;


# response is an encoded message in format "FIND C ......"
#this method find the number of character C in ....
def countOccurence(response):
    res = response.decode()
    
    #remove FIND and followed spaces
    res = re.sub(r'^cs3700spring2019\s+FIND\s+', "", res)
    
    character = res[0]
    
    #remove the ascii character and spaces
    res = re.sub(r'^.*\s+', "", res)
    
    time = res.count(character)
    return time;

def chec():
    print("he")

    
#sendPackage('cs3700spring2019 HELLO 001250783'+'\n', 'cbw.sh', 27993)
#print(re.sub(r'^.*\s+', "", "9  hello"))
#print(re.sub)
if __name__== "__main__":
  main()





















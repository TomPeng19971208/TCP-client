# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys

#./client <-p port> <-s> [hostname] [NEU ID]
#the program takes in 4 arguments, [port, ssl, hostname, NEUID]


  
  
def main():
     print(len(sys.argv))
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
if __name__== "__main__":
  main()        
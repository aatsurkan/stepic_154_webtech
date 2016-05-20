#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Запускается на IP адресе 0.0.0.0 и TCP порту 2222 
# Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
# Закрывает соединение при получении сообщения с текстом close﻿
# Измените ваш echo сервер так, что бы он работать одновременно с 10 клиентами. 
#
# check: $ curl 127.0.0.1:2222 -d "test" --trace-ascii /dev/stdout 

import asyncore                                                                                          
import socket                                                                                            
                                                                                                         
host = ''                                                                                                
port = 2222                                                                                              
                                                                                                         
class EchoHandler(asyncore.dispatcher_with_send):                                                        
    def handle_read(self):                                                                            
        data = self.recv(1024)                                                                    
        if data == 'close':
            self.close()                                                                  
        else:
            self.send(data)
                                                                                                         
class EchoServer(asyncore.dispatcher):                                                                    
    def __init__(self, host, port):                                                                  
        asyncore.dispatcher.__init__(self)                                                        
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)                                    
        self.set_reuse_addr()                                                                    
        self.bind((host, port))                                                                  
        self.listen(15)                                                                          
                                                                                                         
    def handle_accept(self):                                                                          
        pair = self.accept()                                                                      
        if pair is not None:                                                                      
            sock, addr = pair                                                                
            print 'conn', addr                                                                
            handler = EchoHandler(sock)                                                      
                                                                                                         
server = EchoServer(host, port)
asyncore.loop()


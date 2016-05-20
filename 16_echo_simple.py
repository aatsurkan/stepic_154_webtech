#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Запускается на IP адресе 0.0.0.0 и TCP порту 2222 
# Получает сообщения длинной не более 1024 байт и отправляет обратно клиенту
# Закрывает соединение при получении сообщения с текстом close﻿
#
# check: $ curl 127.0.0.1:2222 -d "test" --trace-ascii /dev/stdout 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    if data == 'close': break
    conn.send(data)
conn.close()



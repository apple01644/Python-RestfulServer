import socket, datetime
from typing import Optional, Callable, DefaultDict
import collections
import threading

#host = '127.0.0.1'
#port = 54030

def receive_data():
    pass

class RestfulServer:
    callbacks: DefaultDict = collections.defaultdict(list)
    
    def __init__(self, HOST, PORT):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.run = False
        
        self.thread_accepting = threading.Thread(target=self.accepting, args=(0,))
        
    def start(self):
        self.run = True
        self.thread_accepting.start()

    def accepting(self, dOnTuSeThIsArGuMeNt):
        self.sock.listen()
        while self.run:
            conn, addr = self.sock.accept()
            for func in self.callbacks["accept"]: func(self, conn)
            trd = threading.Thread(target=self.recv, args=(conn, addr))
            trd.start()
                    
        sock.close()

    def recv(self, conn, addr):
        
        data = conn.recv(1048576).decode('utf-8').split('\r\n')                             
        cell = data[0].split(' ')
        method = cell[0]
        path = cell[1]

        header = {}
        body = ''
            
        read_body = False
        for row in data[1:]:
            if row == '':
                read_body = True
            elif read_body:
                body = row
            else:
                cell = row.split(': ')
                header[cell[0]] = cell[1]
            
        for func in self.callbacks["recv_data"]: func(self, conn, method, path, header, body)

    def send(self, conn, status, header, content, content_type, location='/'):
    
        content_raw = content.encode('utf-8')
        data = ''
        data += 'HTTP/1.1 '
        data +=  str(status) + '\r\n'
        data += 'Data: ' + datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT') + '\r\n'
        for key in header.keys():
            data += "{0}: {1}\r\n".format(key, header[key])
        data += 'Connection: close\r\n'
        data += 'Location: {}\r\n'.format(location)
        data += 'Content-Type: {}\r\n'.format(content_type)
        data += 'Content-Length: %d\r\n' % len(content_raw)
        data += '\r\n'
        data += content

        conn.sendall(data.encode('utf-8'))
        
    @staticmethod
    def run_on(event: str):
        def decorator(callback):
            RestfulServer.on(event=event, callback=callback)
            return callback
        return decorator

    @classmethod
    def on(cls, event: str, callback: Callable):
        cls.callbacks[event].append(callback)
            

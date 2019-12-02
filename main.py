import RestfulServer as rs


@rs.RestfulServer.run_on(event="recv_data")
def CB_recvdata(self, conn, method, path, header, body):
    #print(method)
    #print(path)
    #print(header)
    #print(body)

    self.send(conn, 200, {'np' : 'p'}, '<p>It\'s Work!</p>', 'text/html')
    
    
#@rs.RestfulServer.run_on(event="accept")
#def CB_accept(self, conn):
#    pass
    
server = rs.RestfulServer('127.0.0.1', 54030)

server.start()

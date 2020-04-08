import RestfulServer as rs
import datetime

'''
@rs.RestfulServer.run_on(event='accept')
def CB_accept(self, addr):
    print('[{0}]{1}'.format(datetime.datetime.utcnow().strftime('%H:%M:%S')
                    ,addr[0]))
'''

@rs.RestfulServer.run_on(event="/")
def CB_recvdata(self, conn, method, path, header, body):
    #print(method)
    #print(path)
    #print(header)
    #print(body)

    self.send(conn, 200, {'np' : 'p'}, '<p>It\'s Work!</p>', 'text/html')

@rs.RestfulServer.run_on(event="not_found")
def CB_not_Found(self, conn, method, path, header, body):
    self.send(conn, 200, {'np' : 'p'}, '<p>404 Not Found</p>', 'text/html')
    
    
server = rs.RestfulServer('127.0.0.1', 54030)

server.start()

# Python-RestfulServer
Python으로 구현한 Restful Server입니다.

## 예제코드
```
@rs.RestfulServer.run_on(event="recv_data")
def CB_recvdata(self, conn, method, path, header, body):
    self.send(conn, 200, {'np' : 'p'}, '<p>It\'s Work!</p>', 'text/html')
     
server = rs.RestfulServer('127.0.0.1', 54030)

server.start()
```

## Events
### recv_data(connection, method, path, header, body)
클라이언트로 부터 값을 받았을때 발생합니다.
### accept(connection)
클라이언트가 추가 될때 발생합니다.

## Methods
### send(conn, status, header, content, content_type, location='/')
클라이언트에 데이터를 보냅니다.

import socket


class TCPSocket:
    def __init__( ip, port, buffer_size=1024 ):
        self.__ip   = ip
        self.__port = port
        self.__buff = buffer_size

        self.__socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    def start( self ):
        self.__socket.bind( ( self.__ip, self.__port ) )
        self.__socket.listen( 1 )

        conn, addr = self.__socket.accept()
        print( f"Connection from: {addr}" )

        while True:
            packet = conn.recv( self.__buff )

            if data is None:
                break

            print( f"Received:\n {data}" )

            conn.send( data )
        
        conn.close()

if __name__ == "__main__":
    server = TCPSocket( "127.0.0.1", 443, 1024 )

    print( "Starting TCP server!" )
    server.start()
    print( "Closed TCP server..." )
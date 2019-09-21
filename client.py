import socket

class TCPSocket:
    def __init__( ip, port, buffer_size=1024 ):
        self.__ip   = ip
        self.__port = port
        self.__buff = buffer_size

        self.__socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    def start( self ):
        print( "Sending message!" )

        self.__socket.send( "Hello, World!" )

        response = self.__socket.recv( self.__buff )
        print( f"Response: {response}" )
        
        self.__socket.close()

if __name__ == "__main__":
    server = TCPSocket( "127.0.0.1", 443, 1024 )

    print( "Starting TCP server!" )
    server.start()
    print( "Closed TCP server..." )
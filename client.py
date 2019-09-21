import socket
import parser


class ClientSocket():
    def __init__( self, ip:str, port:int, buffer_size:int, mode:str ):
        self.__ip     = ip
        self.__port   = port
        self.__buff   = buffer_size
        self.__packet = b"Hello, World!"

        if mode.lower() == "udp":
            self.__socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        elif mode.lower() == "tcp":
            self.__socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        else:
            raise Exception( "Mode has to be `tcp` or `udp`" )

        if port > 65536:
            raise Exception( "Port is out of range" )

    def start( self ):
        print( "Sending message!" )

        self.__socket.connect( ( self.__ip, self.__port ) )
        self.__socket.send( self.__packet )

        response = self.__socket.recv( self.__buff )
        print( f"Response: {response}" )

        self.__socket.send( b'' )

        self.__socket.close()

if __name__ == "__main__":
    args = parser.parse()

    try:
        client = ClientSocket( args.ip, args.port, 1024, args.mode )
    except Exception as e:
        print( f"An error occured when creating the socket:\n {e}" )
        exit( 1 )

    print( "Starting TCP socket!" )

    try:
        client.start()
    except Exception as e:
        print( f"An error occured when starting the socket:\n {e}" )
        exit( 1 )

    print( "Closed TCP socket..." )

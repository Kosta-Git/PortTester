import socket
import parser


class ServerSocket:
    def __init__( self, ip:str, port:int, buffer_size:int, mode:str ):
        self.__ip   = ip
        self.__port = port
        self.__buff = buffer_size
        self.__mode = mode.lower()

        if mode.lower() == "udp":
            self.__socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        elif mode.lower() == "tcp":
            self.__socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        else:
            raise Exception( "Mode has to be `tcp` or `udp`" )

        if port > 65536:
            raise Exception( "Port is out of range" )

    def start( self ):
        self.__bind()

        if self.__mode == "tcp":
            self.__start_tcp()
        else:
            self.__start_udp()
    
    def __start_tcp( self ):
        self.__socket.listen( 1 )

        conn, addr = self.__socket.accept()
        print( f"Connection from: {addr[0]}" )

        while True:
            packet = conn.recv( self.__buff )

            if packet is None or packet == b'':
                break

            print( f"Received:\n\t {str( packet )}" )

            conn.send( packet )
        
        conn.close()
    
    def __start_udp( self ):
        while True:
            packet = self.__socket.recvfrom( self.__buff )

            if packet[0] is None or packet[0] == b'':
                break

            print( f"Received:\n\t {str( packet[0] )}" )

            self.__socket.sendto( packet[0], packet[1] )

    def __bind( self ):
        self.__socket.bind( ( self.__ip, self.__port ) )

        socket_info = self.__socket.getsockname()
        print( f"Socket bound.\n\tip: {socket_info[0]}\n\tport: {socket_info[1]}" )


if __name__ == "__main__":
    args = parser.parse()

    try:
        server = ServerSocket( args.ip, args.port, 1024, args.mode )
    except Exception as e:
        print( f"An error occured when creating the socket:\n {e}" )
        exit( 1 )

    print( f"Starting {args.mode} socket!" )

    try:
        server.start()
    except Exception as e:
        print( f"An error occured when binding the socket:\n {e}" )
        exit( 1 )

    print( f"Closed {args.mode} socket..." )
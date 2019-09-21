import argparse

def parse():
    parser = argparse.ArgumentParser()
    
    parser.add_argument( "-i", "--ip", help="Specify ip", type=str, default="127.0.0.1" )
    parser.add_argument( "-m", "--mode", help="Specify UDP or TCP", type=str, required=True )
    parser.add_argument( "-p", "--port", help="Specify port", type=int, required=True )

    return parser.parse_args()
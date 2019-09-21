# Python port tester

## Usage

### host.py usage

`python3 host.py -m UDP -p 666`

`-m` or `--mode` takes udp or tcp

`-p` or `--port` takes a port number

`-i` or `--ip` takes an ip (optional default is 127.0.0.1) consider using 0.0.0.0

NOTE: This script requires admin privileges!

### client.py usage

`python3 client.py -m UDP -p 666`

`-m` or `--mode` takes udp or tcp

`-p` or `--port` takes a port number

`-i` or `--ip` takes an ip (optional default is 127.0.0.1)

NOTE: This script requires admin privileges!

## Additional comments

Please always run the host before the client.
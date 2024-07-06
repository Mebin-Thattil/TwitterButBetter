import socket

hostname = socket.gethostname()

def primary_ip():
    local_hostname = socket.gethostname()
    primary_ip = [ip for ip in socket.gethostbyname_ex(local_hostname)[2] if not ip.startswith("127.")][:1][0]
    return primary_ip

custom_ip = ''
ip = primary_ip()
#ip = custom_ip
port = 8090

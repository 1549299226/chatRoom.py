import socket

def test():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8090))
    
    while True:
        msg = input('请输入:')
        client_socket.send(msg.encode('utf-8'))
        # recv_data = client_socket.recv(512)
        # print(recv_data.decode('utf-8'))
    
    
    client_socket.close()
    
    
if __name__ == '__main__':
    test()
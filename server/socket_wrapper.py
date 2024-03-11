
class SocketWrapper(object):
    """套接字包装类"""
    def __init__ (self, sock):
        if not hasattr(sock, 'recv') or not hasattr(sock, 'send'):
            raise ValueError("传入的对象缺少 'recv' 或 'send' 方法")
        self.sock = sock
        
        
        self.sock = sock
        
    def recv_data(self):
        """接受数据并解码为字符串"""
        try:
            return self.send_recv(512).decode('utf-8')
        except:
            return ""
        
        
    
    def send_data(self, message):
        """把字符串编码并发送给客户端"""
        return self.sock.send(message.encode('utf-8'))
         
    def close(self):
        """关闭套接字"""
        self.sock.close()
        
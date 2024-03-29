from server_socket import ServerSocket
from server_socket import SocketWrapper
from threading import Thread

class Server(object):
    """服务器核心类"""
    def __init__(self):
        #创建服务器套接字
        self.server_socket = ServerSocket()
    
    def startup(self):
        while True:
            """获取客户端链接，并提供服务"""
            #获取客户端连接
            print('正在获取客户端连接...')
            soc, addr = self.server_socket.accept() 
            print('获取到客户端连接')
            
            #生成使用套接字包装对象
            client_soc = SocketWrapper(soc)
            
            Thread(target=lambda: self.request_handle(client_soc)).start()
            
            #收发消息
        
            #     #关闭套接字
            # soc.close()
        
        
    def request_handle(self, client_soc):
        """线程的任务函数，收发消息"""
        while True:
            #接收客户端数据
            recv_data = client_soc.recv_data()
            if not recv_data:
                #没有收到数据客户端应该已经关闭
                self.remove_offline_user(client_soc)
                client_soc.close()
                break
            # print(msg)
            # client_soc.send_data('服务器接收到的是:' + msg)
            #解析数据
            
            parse_data = self.parse_erequest_text(recv_data)
            
            #分析请求类型，并根据请求类型调用相应的处理函数
            print('获取到解析后内容:%s'  % parse_data)
            
            
    def remove_offline_user(self, client_soc):
        """客户端下线的处理"""
        print("有客户下线了")
        
        
    def parse_erequest_text(self, recv_data):
        """解析客户端发送的数据"""
        print('解析客户端数据：'+ recv_data)
        
        
if __name__ == '__main__':
    Server().startup()        
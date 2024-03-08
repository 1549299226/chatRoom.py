from config import *

class ResponseProtocol(object):
    """服务器响应协议 格式的字符串处理"""
    @staticmethod
    def response_login_result(result, nickname, username):
        """生成用户登陆的结果字符串"""
        """
        result : 登录结果 0表示登陆失败 1表示成功
        nickname: 登陆用户的昵称，登陆失败为空
        username: 登陆用户的账号。 登陆失败为空
        return : 返回给用户的登录结果协议字符串 
        """
        return DELIMITER.join([RESPONSE_LOGIN_RESULT, result, nickname, username])
    
    
    @staticmethod
    def response_chat(nickname, messages):
        """
        返回给用户的消息字符串
        nickname:发送消息的用户名
        messages:消息正文
        return: 返回给用户的消息字符串
        """
        return DELIMITER.join([RESPONSE_CHAT, nickname, messages])

 
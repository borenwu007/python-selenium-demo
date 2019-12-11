#encoding=UTF-8
import http.client
import base64

def base_code(username, password):
    str = '%s:%s' % (username, password)
    encodestr = base64.b64encode(str.encode('utf-8'))
    return '%s' % encodestr.decode()


if __name__ == '__main__':
    username = "borenwu@163.com"  
    password = "871120wbrW"  # 您的密码
    proxy_ip = "125.87.110.129"  # 代理ip，通过http://h.wandouip.com/get获得
    proxy_port = "5412"  # 代理端口号
    headers = {
        'Proxy-Authorization': 'Basic %s' % (base_code(username, password))
    }
    url = 'https://t00y.com/file/21552682-413069894'
    try :
        con = http.client.HTTPConnection(proxy_ip, port=proxy_port, timeout=10)
        con.request("GET", url, headers=headers)
        resu = con.getresponse()
        text = resu.read().decode("utf-8", errors="ignore")
        print(text)
    except Exception as e:
        print(e)
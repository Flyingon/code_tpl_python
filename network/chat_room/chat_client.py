#coding=utf-8
# 由于实验都在本机上运行, 所以server addr == client addr
import socket,select,threading,sys
host = "www.yuanzhaoyi.cn" #socket.gethostname()
# client_addr = (host, 5963)  # equals server_addr()
client_addr = (host, 3000)

# 倾听其他成员谈话
def listening(cs):
    inputs = [cs]
    while True:
        rlist,wlist,elist = select.select(inputs, [], [])
        # client socket就是用来收发数据的, 由于只有这个waitable 对象, 所以不必迭代
        if cs in rlist:
            try:
                # 打印从服务器收到的数据
                print(cs.recv(1024))
            except socket.error:
                print("socket is error")
                exit()

# 发言
def speak(cs):
    while True:
        try:
            data = input()
        except Exception as e:
            print(r"can't input")
            exit()
        # if data == "exit":
        #     cs.close()
        #     break
        try:
            cs.send(data.encode('utf-8'))
        except Exception as e:
            exit()


def main():
    # client socket
    cs = socket.socket()
    cs.connect(client_addr)
    # 分别启动听和说线程
    t = threading.Thread(target=listening,args=(cs,))
    t.start()

    t1 = threading.Thread(target=speak,args=(cs,))
    t1.start()

if __name__ == "__main__":
    main()
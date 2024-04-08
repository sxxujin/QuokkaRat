import socket

host = "172.17.0.3"
port = 8282

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    message = s.recv(1024).decode()
    print(f"상대부터 온 메세지 : {message}")

    data = input("당신의 메세지를 입력하세요: ")

    s.send(data.encode())
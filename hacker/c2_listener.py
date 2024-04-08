import socket

host = '0.0.0.0'
port = 8282

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)
print(f"Listening for incoming connections on {host}:{port}...")
conn, addr = s.accept()
print(f"Connection established with {addr}")

while True:
    command = input("Enter Command: ")
    conn.send(command.encode())
    output = conn.recv(1024).decode()
    print(f'recv : {output}')

   
 # 연결 닫기
conn.close()

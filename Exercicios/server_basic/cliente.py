import socket
cmd = input("cmd > ")
while cmd != "/off":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8888))
    s.send(cmd.encode("utf-8"))
    msg = s.recv(1024)
    print("\nResposta:", msg.decode("utf-8"))
    cmd = input("\ncmd > ")
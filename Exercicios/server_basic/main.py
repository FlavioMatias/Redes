from servidor import Server

Server.config(
    ip = 'localhost',
    port = 8888,
    protocol = 'tcp',
    backlog = 1
)

Server.ligar()
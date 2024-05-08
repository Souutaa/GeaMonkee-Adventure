import socket
from _thread import *
from constants import *
from utils import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server started")

pos = [(0, 0, 0, 1), (100, 100, 0, 1)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if (player == 1):
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: ", data)
                print("Sending: ", reply)
            conn.send(str.encode(make_pos(reply)))
        except:
            break
    print("Lost connection")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

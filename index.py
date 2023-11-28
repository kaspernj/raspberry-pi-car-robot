import socket

def threaded(conn):
  while True:
    data = conn.recv(4096)

    if not data:
      print("Bye")
      break

  conn.close()

def Main():
  host = socket.gethostname()
  port = 9687

  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((host, port))
  server_socket.listen(1)

  print("Listening on " + host + ":" + str(port))

  while True:
    conn, address = server_socket.accept()

    start_new_thread(threaded, (conn,))

if __name__ == "__main__":
  Main()

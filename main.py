import socket, ssl


HOST, PORT = 'localhost', 2096

def handle(conn):
    conn.write(b'Hi, this is SSL connection. Secured by ssl self signed cert!\n')
    print(conn.recv().decode())

def main():

    sock = socket.socket(socket.AF_INET)

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    context.verify_mode=ssl.CERT_NONE

    conn = context.wrap_socket(sock, server_hostname=HOST)

    try:
        conn.connect((HOST, PORT))
        handle(conn)
    finally:
        conn.close()

if __name__ == '__main__':
    main()


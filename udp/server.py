import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0.0.0.0', 5001))
    print("Server is listening on port 5001")

    while True:
        data, addr = server.recvfrom(1024)
        message = data.decode()
        print(f"Received from client {addr}: {message}")
        reversed_message = message[::-1]
        server.sendto(reversed_message.encode(), addr)
        print(f"Sent to client {addr}: {reversed_message}")

if __name__ == "__main__":
    start_server()

import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 5001)
    
    while True:
        message = input("Enter string to reverse: ")
        if message.lower() == 'exit':
            break
        client.sendto(message.encode(), server_address)
        data, _ = client.recvfrom(1024)
        print(f"Received from server: {data.decode()}")
    
    client.close()

if __name__ == "__main__":
    start_client()

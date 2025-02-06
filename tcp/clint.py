import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5001))
    
    while True:
        message = input("Enter string to reverse: ")
        if message.lower() == 'exit':
            break
        client.send(message.encode())
        
        
        response = client.recv(1024).decode()
        print(f"Received from server: {response}")
    
    client.close()

if __name__ == "__main__":
    start_client()

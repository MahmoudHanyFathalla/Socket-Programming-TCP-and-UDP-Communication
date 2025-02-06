# Socket Programming Project: TCP and UDP Communication

## Overview

This project demonstrates the implementation of basic client-server communication using both **TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** in Python. The project is divided into two main directories, `tcp/` and `udp/`, each containing a client and server script that showcase how to establish communication between a client and a server using the respective protocol.

The **TCP** implementation provides a reliable, connection-oriented communication channel, while the **UDP** implementation offers a faster, connectionless communication method. Both implementations allow the client to send a string to the server, which reverses the string and sends it back to the client.

## Project Structure

The project is organized into two main directories, each containing the client and server scripts for TCP and UDP communication:

```
sockets/
   ├── tcp/
   │   ├── clint.py
   │   └── server.py
   └── udp/
       ├── clint.py
       └── server.py
```

### TCP Implementation

The TCP implementation provides a reliable, connection-oriented communication between the client and server. The server listens for incoming connections, and once a connection is established, it handles client requests in a separate thread, allowing multiple clients to connect simultaneously.

#### Files in `tcp/` Directory

- **`clint.py`**: The TCP client script.
  - Connects to the server running on `localhost` at port `5001`.
  - Sends a string to the server and waits for the reversed string response.
  - The client can send multiple strings until the user types `exit` to terminate the connection.

- **`server.py`**: The TCP server script.
  - Listens for incoming TCP connections on port `5001`.
  - Handles each client connection in a separate thread.
  - Reverses the received string and sends it back to the client.

### UDP Implementation

The UDP implementation provides a faster, connectionless communication method. The server listens for incoming datagrams, processes the received data, and sends back the reversed string to the client.

#### Files in `udp/` Directory

- **`clint.py`**: The UDP client script.
  - Sends a string to the server running on `localhost` at port `5001`.
  - Waits for the reversed string response from the server.
  - The client can send multiple strings until the user types `exit` to terminate the communication.

- **`server.py`**: The UDP server script.
  - Listens for incoming UDP datagrams on port `5001`.
  - Reverses the received string and sends it back to the client.

## How to Run the Project

### Prerequisites

- Python 3.x installed on your system.
- Basic understanding of socket programming.

### Running the TCP Implementation

1. **Start the TCP Server**:
   - Navigate to the `tcp/` directory.
   - Run the server script:
     ```bash
     python server.py
     ```
   - The server will start listening on port `5001`.

2. **Start the TCP Client**:
   - In a new terminal, navigate to the `tcp/` directory.
   - Run the client script:
     ```bash
     python clint.py
     ```
   - Enter a string to send to the server. The server will respond with the reversed string.
   - Type `exit` to terminate the client.

### Running the UDP Implementation

1. **Start the UDP Server**:
   - Navigate to the `udp/` directory.
   - Run the server script:
     ```bash
     python server.py
     ```
   - The server will start listening on port `5001`.

2. **Start the UDP Client**:
   - In a new terminal, navigate to the `udp/` directory.
   - Run the client script:
     ```bash
     python clint.py
     ```
   - Enter a string to send to the server. The server will respond with the reversed string.
   - Type `exit` to terminate the client.

## Code Explanation

### TCP Client (`tcp/clint.py`)

- The client creates a TCP socket and connects to the server at `localhost:5001`.
- It sends a string to the server and waits for the reversed string response.
- The client continues to send strings until the user types `exit`.

### TCP Server (`tcp/server.py`)

- The server creates a TCP socket and binds it to `0.0.0.0:5001`.
- It listens for incoming connections and handles each client in a separate thread.
- The server reverses the received string and sends it back to the client.

### UDP Client (`udp/clint.py`)

- The client creates a UDP socket and sends a string to the server at `localhost:5001`.
- It waits for the reversed string response from the server.
- The client continues to send strings until the user types `exit`.

### UDP Server (`udp/server.py`)

- The server creates a UDP socket and binds it to `0.0.0.0:5001`.
- It listens for incoming datagrams, reverses the received string, and sends it back to the client.

## Key Differences Between TCP and UDP

- **TCP**:
  - Connection-oriented protocol.
  - Reliable, ensures data delivery.
  - Slower due to connection establishment and error checking.
  - Used in applications where data integrity is critical (e.g., web browsing, email).

- **UDP**:
  - Connectionless protocol.
  - Faster, but does not guarantee data delivery.
  - Used in applications where speed is more important than reliability (e.g., video streaming, online gaming).

## Conclusion

This project provides a hands-on introduction to socket programming in Python, demonstrating both TCP and UDP communication. By running the provided scripts, you can observe the differences between the two protocols and understand their use cases. This project serves as a foundation for building more complex networked applications.

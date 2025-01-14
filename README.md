# socket_programming

# Socket Programming in Python

This project demonstrates socket programming concepts in Python through three different applications:

1. **TCP Echo Server-Client Application**
2. **Mathematical Expression Evaluation Server-Client Application**
3. **Multi-Client Chat Application**

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Applications Overview](#applications-overview)
  - [1. TCP Echo Server-Client Application](#1-tcp-echo-server-client-application)
  - [2. Mathematical Expression Evaluation Server-Client Application](#2-mathematical-expression-evaluation-server-client-application)
  - [3. Multi-Client Chat Application](#3-multi-client-chat-application)
- [How to Run](#how-to-run)

---

## Prerequisites
1. Python 3.x installed on your system. If not installed, download and install it from [Python's official site](https://www.python.org/).
2. Basic knowledge of Python programming and networking concepts.

---

## Setup Instructions
1. Clone or download this repository.
2. Navigate to the project directory using your terminal or command prompt.
3. Install any required Python modules using:
   ```bash
   pip install -r requirements.txt
   ```
   (No external libraries are used, so this step might be unnecessary.)

---

## Applications Overview

### 1. TCP Echo Server-Client Application
This application acts as an echo service, where the server receives a message from the client and sends the same message back.

#### Files:
- `TCP_Server.py`
- `TCP_Client.py`

#### Features:
- The server listens for connections on a specified IP and port.
- The client sends a message to the server, which echoes it back.
- Demonstrates basic TCP communication.

---

### 2. Mathematical Expression Evaluation Server-Client Application
This application allows the client to send a mathematical expression to the server for evaluation. The server computes the result and returns it to the client.

#### Files:
- `Calc_Server.py`
- `Calc_Client.py`

#### Features:
- The server listens for incoming connections and evaluates expressions sent by clients.
- The client can send multiple expressions or terminate the connection by typing `exit`.

---

### 3. Multi-Client Chat Application
This application allows multiple clients to connect to a server and exchange messages in real-time.

#### Files:
- `Chat_Server.py`
- `Chat_Client.py`

#### Features:
- **Server**:
  - Dynamically retrieves its IP address and listens on a specified port.
  - Supports multiple clients using threading.
  - Broadcasts messages from one client to all others.
  - Notifies users when a new client joins or leaves the chat.
  - Handles client disconnections gracefully.
- **Client**:
  - Prompts users to enter their username upon connection.
  - Displays active users when joining the chat.
  - Allows users to send and receive messages in real-time.
  - Exits the chat gracefully by typing `exit`.

---

## How to Run

### 1. TCP Echo Server-Client Application
1. Start the server:
   ```bash
   python TCP_Server.py
   ```
2. Start the client:
   ```bash
   python TCP_Client.py
   ```
3. Follow the on-screen instructions to send and receive messages.

### 2. Mathematical Expression Evaluation Server-Client Application
1. Start the server:
   ```bash
   python Calc_Server.py
   ```
2. Start the client:
   ```bash
   python Calc_Client.py
   ```
3. Enter mathematical expressions as prompted. Type `exit` to terminate the session.

### 3. Multi-Client Chat Application
1. Start the server:
   ```bash
   python Chat_Server.py
   ```
2. Start one or more clients:
   ```bash
   python Chat_Client.py
   ```
3. Enter a username for each client and start chatting.
4. Type `exit` to leave the chat.

---

Feel free to explore the code and enhance the functionalities. Happy coding!


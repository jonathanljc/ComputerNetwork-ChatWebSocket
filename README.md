# 📜 Python Socket Programming: Chat Application

## 📝 Project Overview
This project demonstrates a **Chat Application** using **Python Socket Programming**. The application consists of a `server` and multiple `clients`. It supports real-time communication, allowing multiple clients to connect to the server and exchange messages. This project includes essential features as well as optional extensions for enhanced functionality.

This project was developed as part of the **INF1006 Computer Networks Assignment 2** at SIT.

---

## ✨ Features

### Basic Features
1. **🧑 Username Assignment**:
   - Clients must enter a unique username upon connecting.
   - Server responds with `[Welcome <username>]`.
   - If the username is already in use, the server prompts the client to enter another.

2. **📢 Message Broadcasting**:
   - Messages sent by clients are prefixed with their username and broadcast to all connected clients.  
     Example: `[John:] Hello everyone!`

3. **🔌 Client Disconnection**:
   - Clients can disconnect using `@quit`.
   - Server notifies all clients when a user exits the chat.  
     Example: `[John exited]`

4. **📋 User List**:
   - Clients can view all connected usernames by issuing the command `@names`.  
     Example: `[Connected users: John, Peter, Stella]`

5. **💬 Personal Messaging**:
   - Users can send direct messages to specific clients using `@<username> <message>`.  
     Example: `@Stella Are you free next Tuesday?`

### Optional Features (Extensions)
1. **👥 Group Chat**:
   - Create a group using `@group set <group_name> <user1,user2,...>`.
   - Send messages to the group using `@group send <group_name> <message>`.
   - Leave or delete groups with `@group leave <group_name>` and `@group delete <group_name>`.

2. **🔧 Group Management**:
   - Group owners can add members with `@add <group_name> <user>`.
   - Owners can remove users from a group using `@kick <group_name> <user>`.

3. **🆘 Help Command**:
   - Display available commands using `@help`.

---

## 📁 File Structure

### 1. `ServerFinal`
- **Description**: Handles client connections, broadcasts messages, manages group chat functionality, and processes client commands.
- **Key Functions**:
  - **`start()`**: Starts the server and listens for incoming connections.
  - **`run()`**: Accepts client connections and initializes threads for each client.
  - **Group Commands**: Functions like `handle_group_setup`, `handle_group_send`, `handle_group_delete`, and more manage group-specific operations.
  - **Error Handling**: Prevents invalid or duplicate usernames and group names.

### 2. `ClientFinal`
- **Description**: Manages client-side operations like connecting to the server, sending messages, and receiving updates.
- **Key Functions**:
  - **`receive_messages()`**: Listens for and displays messages from the server.
  - **`send_messages()`**: Allows the client to send messages or execute commands.
  - **`main()`**: Manages client initialization, username assignment, and server connection.

---

## 🛠️ Commands

### General Commands
| **Command**                  | **Description**                                           |
|------------------------------|-----------------------------------------------------------|
| `@quit`                     | Exit the chat.                                            |
| `@names`                    | List all connected users.                                 |
| `@<username> <message>`     | Send a private message to a user.                         |
| `@help`                     | Display a list of available commands.                     |

### Group Commands
| **Command**                           | **Description**                                           |
|---------------------------------------|-----------------------------------------------------------|
| `@group set <group_name> <users>`     | Create a group with the specified name and users.         |
| `@group send <group_name> <msg>`      | Send a message to the group.                              |
| `@group delete <group_name>`          | Delete a group.                                           |
| `@group leave <group_name>`           | Leave a group.                                            |
| `@kick <group_name> <user>`           | Remove a user from a group (group owner only).            |
| `@add <group_name> <user>`            | Add a user to a group (group owner only).                 |

---

## 🚀 Prerequisites

To run this chat application, ensure you have the following:

1. **Python**: Version 3.x installed on your system.  
   - [Download Python](https://www.python.org/downloads/)

2. **Built-in Libraries**:
   - `socket`: Handles network communication.
   - `threading`: Manages multiple clients concurrently.
   - `re`: Used for input validation (group names and commands).

3. **Networking Setup**:
   - Use `localhost` (`127.0.0.1`) for testing on the same machine.
   - Ensure the server's IP address and port number are reachable if running across machines.

4. **System Configuration**:
   - Open separate terminal/command prompts for the server and clients.
   - Allow the chosen port through any firewall if running on a local network.

---

## 📹 Demonstration Video

Watch the project demonstration video on YouTube:  
[**Chat Application Demo**](https://www.youtube.com/watch?v=a226wXnOiuY)

---

## 👥 Contributors

### Group 19:
| **Name**             | **ID**       | **Email**                              |
|-----------------------|--------------|----------------------------------------|
| Jonathan Lim         | 2300923      | 2300923@sit.singaporetech.edu.sg       |
| Felix Chang          | 2301105      | 2301105@sit.singaporetech.edu.sg       |
| Chew Liang Zhi       | 2300948      | 2300948@sit.singaporetech.edu.sg       |
| Ryan Oh              | 2300916      | 2300916@sit.singaporetech.edu.sg       |
| Darryl Ong           | 2301402      | 2301402@sit.singaporetech.edu.sg       |
| James Gonzales       | 2301136      | 2301136@sit.singaporetech.edu.sg       |

---

**Note**: This project uses only Python's built-in libraries. No additional installations are required.



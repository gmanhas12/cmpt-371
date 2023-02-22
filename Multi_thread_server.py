import socket
import threading
import os
import re
import time
from datetime import datetime

# Define the port to listen on
PORT = 8080

prt_arr = [8080 + x + 1 for x in range(15)]

# Create a request handler that serves the HTML file and handles HTTP codes
def handle_client(client_socket, newport):
    # Open a new port for the client to communicate on

    print("client on IP 127.0.0.1, Port:", newport)

    # Read the request data from the client
    request_data = client_socket.recv(1024).decode('utf-8')

    # Parse the request data to get the requested file path and the client's previous modification timestamp
    file_path, last_modified, req_type, version = parse_request(request_data)

    # If the request is malformed, send a 400 response
    if malformed(file_path, req_type, version):
        response = "HTTP/1.1 400 Bad Request\n"
        response += "\n"
        client_socket.send(response.encode("utf-8"))
        client_socket.close()
        prt_arr.append(newport)
        return

    # If the requested file has not been modified, send a 304 response
    
    if not modified(file_path,last_modified):
        response = "HTTP/1.1 304 Not Modified\n"
        response += "\n"
        client_socket.send(response.encode("utf-8"))
        client_socket.close()
        prt_arr.append(newport)
        return

    

    try:
        # Open the HTML file and read its contents
        with open(file_path, "r") as f:
            html = f.read()
    except FileNotFoundError:
        # If the file does not exist, send a 404 response
        response = "HTTP/1.1 404 Not Found\n"
        response += "Content-Type: text/html\n"
        response += "\n"
        response += "<h1>404 Not Found</h1>"
    else:
        # Set the response code to 200 (OK)
        response = "HTTP/1.1 200 OK\n"

        # Set the content type to text/html
        response += "Content-Type: text/html\n"

        # End the headers
        response += "\n"

        # Add the HTML file to the response
        response += html

    # Send the response to the client
    client_socket.send(response.encode("utf-8"))

    # Close the client socket

    time.sleep(5)

    client_socket.close()
    prt_arr.append(newport)
    return


def malformed(file_path, req_type, version):

    # Check if the first line is empty or does not contain a valid HTTP method
    if not req_type or req_type.split()[0] not in ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]:
        return True
    
    # Check if the second line is empty or does not contain a valid HTTP path
    if not file_path:
        return True

    # Check if the third line is empty or does not contain a valid HTTP version
    if not version or version.split()[0] not in ["HTTP/1.0", "HTTP/1.1"]:
        return True

    # If none of the checks failed, the request is not malformed
    return False

def modified(file_path, last_modified):

    # Get the current modification timestamp of the file
    try:
        current_modified = os.stat(file_path).st_mtime
        # Check if the file has been modified since the last time it was requested by the same client
        if current_modified > last_modified:
            last_modified = current_modified
            return True

        # If the file has not been modified, return True
        return False
    except:
        return True

def parse_request(request_data):
    # Split the request data into lines

    lines = request_data.split(" ")
    # Extract the requested file path from the first line
    file_path = lines[1]
    if len(file_path) and file_path[0] == '/':
        file_path = file_path[1:]

    # Extract the client's previous modification timestamp from the "If-Modified-Since" request header
    last_modified = re.search(r"If-Modified-Since: (.*)", request_data)
    last_modified = datetime.timestamp(datetime.strptime(last_modified.group(1), '%a, %d %b %Y %I:%M:%S %Z')) if last_modified else 0
    

    return file_path, last_modified, lines[0], lines[2]

def request_timeout(client_socket,newport):
    # Set the response code to 408 (Request Timeout)
    response = "HTTP/1.1 408 Request Timeout\n"

    # Set the content type to text/html
    response += "Content-Type: text/html\n"

    # End the headers
    response += "\n"

    # Add an error message to the response
    response += "<h1>408 Request Timeout</h1>"

    # Send the response to the client
    client_socket.send(response.encode("utf-8"))

    # Close the client socket
    client_socket.close()
    prt_arr.append(newport)
    return

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to the specified IP address and port
server_socket.bind(("127.0.0.1", PORT))

# Start listening for incoming connections
server_socket.listen()

print("Listening on IP 127.0.0.1, port {}...".format(PORT))

while True:
    # Accept an incoming connection
    
    client_socket, client_address = server_socket.accept()

    thread_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    newport = 9999
    try:
        newport = prt_arr.pop()
    except:
        continue
    thread_socket.bind(('127.0.0.1', newport))
    thread_socket.listen()
    # Create new thread for client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,newport))

    #start the thread
    client_thread.start()
    start_time = time.time()
    
    if time.time() - start_time > 5:
        # Send a 408 (Request Timeout) response
        request_timeout(client_socket, newport)
        


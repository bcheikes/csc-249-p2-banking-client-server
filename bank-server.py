#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def process_client_msg(msg_bytes):
    return

def send_response_to_client(code, result):
    return

def run_bank_server():
    print("server starting - listening for connections at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected established with {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                client_msg = data.decode()
                code, result = process_client_msg(client_msg)
                send_response_to_client(code, result)
                if code == -1:
                    print("server exiting on error code -1")
                    break

if __name__ == "__main__":
    run_bank_server()
    print("bank server exiting...")
#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

class Bank_Account:
    acct_number = ''
    acct_pin = 0000
    

    @staticmethod
    def split_name(name_string):
        # this is an internal utility function that takes a name string with internal underscore separators.
        # it splits the string at the first and (if found) second underscore, returning a list of up to three substrings.
        # we return the list with the individual parts capitalized.
        if '_' not in name_string:
            # probably should raise an exception here
            return name_string
        # break the name_string into a list, using underscore as delimiter. 2 splits at most.
        parts = name_string.split('_',2)
        # return the list of the name parts with each part capitalized
        return [n.capitalize() for n in parts]

    def __init__(self, id_num, email):
        # initialize the state variables of a new Leader instance
        self.id_num = id_num
        self.known = True
        self.email = email
        self.names = list()
        self.committees = list()
        if len(email) > 0:
            self.email = email.lower()
        self.trip_dates = set()
        self.trips_as_leader = 0
        self.trips_as_coleader = 0
        self.trips_cancelled = 0

    def primary_name(self):
        return self.names[0] if len(self.names) > 0 else ''

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
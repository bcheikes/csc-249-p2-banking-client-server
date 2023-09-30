#!/usr/bin/env python3
#
# Bank Server application
# Jimmy da Geek

import socket

HOST = "127.0.0.1"      # Standard loopback interface address (localhost)
PORT = 65432            # Port to listen on (non-privileged ports are > 1023)
ALL_ACCOUNTS = dict()   # initialize an empty dictionary
ACCT_FILE = "accounts.txt"

# Helper functions for Bank Server
def acctNumberIsValid(ac_num):
    # a valid account number must be a string, lenth = 8, and match the format AA-NNNNN where AA are two alphabetic characters
    # and NNNNN are five numeric characters
    return isinstance(ac_num, str) and \
        len(ac_num) == 8 and \
        ac_num[2] == '-' and \
        ac_num[:2].isalpha() and \
        ac_num[3:8].isdigit()

def acctPinIsValid(pin):
    return (isinstance(pin, str) and \
        len(pin) == 4 and \
        pin.isdigit())

def amountIsValid(amount):
    # For an amount to be valid it must be a positive float() value with at most two decimal places
    return isinstance(amount, float) and (round(amount, 2) == amount) and (amount >= 0)

# Individual bank accounts are stored as BankAccount instances
class BankAccount:
    acct_number = ''
    acct_pin = ''
    acct_balance = 0.0
    
    def __init__(self, ac_num = "zz-00000", ac_pin = "0000", bal = 0.0):
        # initialize the state variables of a new BankAccount instance
        if acctNumberIsValid(ac_num):
            self.acct_number = ac_num
        if acctPinIsValid(ac_pin):
            self.acct_pin = ac_pin
        if amountIsValid(bal):
            self.acct_balance = bal

    def deposit(self, amount):
        # if the amount is valid, then update the acct_balance
        # return three values: self, success_code, current balance
        # Success codes:
        #  0: valid result
        #  1: invalid amount
        success_code = 0
        if not amountIsValid(amount):
            success_code = 1
        else:
            # valid amount, so add it to balance and set succes_code 1
            self.acct_balance += amount
        return self, success_code, self.acct_balance

    def withdraw(self, amount):
        # if the amount is valid, then update the acct_balance
        # return three values: self, success_code, current balance
        # Success codes:
        #  0: valid result
        #  1: invalid amount
        #  2: attempt to overdraw account
        success_code = 0
        if not amountIsValid(amount):
            # invalid amount, return error 
             success_code = 1
        elif amount > self.acct_balance:
            # attempted overdraft
            success_code = 2
        else:
            # all checks out, subtract amount from the balance
            self.acct_balance -= amount
        return self, success_code, self.acct_balance

def get_acct(acct_num):
    # Lookup acct_num in the ALL_ACCOUNTS database and return the account object if it's found.
    # Return False if the acct_num is invalid. If the 
    if acctNumberIsValid(acct_num) and (acct_num in ALL_ACCOUNTS):
        return ALL_ACCOUNTS[acct_num]
    else:
        return False

def load_account(num_str, pin_str, bal_str):
    # all arguments are strings
    try:
        bal = float(bal_str)
        if acctNumberIsValid(num_str) and not get_acct(num_str):
        # We have a valid new account number not previously loaded
            new_acct = BankAccount(num_str, pin_str, bal)
            ALL_ACCOUNTS[num_str] = new_acct
            print(f"loaded account '{num_str}'")
            return True
    except ValueError:
        print(f"error loading acct '{num_str}': balance value not a float")
        return False
    
def load_all_accounts(acct_file = "accounts.txt"):
    print(f"loading account data from file: {acct_file}")
    with open(acct_file, "r") as f:
        while True:
            line = f.readline()
            if not line:
                # we're done
                break
            if line[0] == "#":
                # comment line, no error, ignore
                continue
            # convert all alpha characters to lowercase and remove whitespace, then split on comma
            acct_data = line.lower().strip().split(',')
            if len(acct_data) != 3:
                print("ERROR: invalid entry in account file: '{line}' - IGNORED")
                continue
            load_account(acct_data[0], acct_data[1], acct_data[2])
    print("finished loading account data")
    return True

# Bank Server network operations
# All code involved in supporting the bank server's network communications goes in this section
def process_client_msg(msg_bytes):
    return

def send_response_to_client(code, result):
    return

def run_bank_server():
    # Needs to be written!
    load_all_accounts(ACCT_FILE)

if __name__ == "__main__":
    run_bank_server()
    print("bank server exiting...")